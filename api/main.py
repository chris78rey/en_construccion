from __future__ import annotations

import os
import secrets
import sqlite3
import threading
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Literal

from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel, EmailStr, Field


Topic = Literal[
    "machine-learning",
    "analitica-bi",
    "ingenieria-datos",
    "documentacion",
    "infra-coolify",
    "capacitacion",
    "otro",
]


class CreateContactRequest(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    email: EmailStr
    subject: str = Field(min_length=2, max_length=200)
    topic: Topic
    message: str = Field(min_length=5, max_length=5000)


class CreateContactResponse(BaseModel):
    id: int
    created_at: str


class Contact(BaseModel):
    id: int
    created_at: str
    name: str
    email: str
    subject: str
    topic: Topic
    message: str


class ListContactsResponse(BaseModel):
    items: list[Contact]


@dataclass(frozen=True)
class Settings:
    db_path: str
    admin_user: str
    admin_password: str


def load_settings() -> Settings:
    return Settings(
        db_path=os.environ.get("DB_PATH", "/data/contacts.db"),
        admin_user=os.environ.get("ADMIN_USER", ""),
        admin_password=os.environ.get("ADMIN_PASSWORD", ""),
    )


security = HTTPBasic()
_db_lock = threading.Lock()


def _connect(db_path: str) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def _init_db(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS contacts (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          created_at TEXT NOT NULL,
          name TEXT NOT NULL,
          email TEXT NOT NULL,
          subject TEXT NOT NULL,
          topic TEXT NOT NULL,
          message TEXT NOT NULL
        )
        """
    )
    conn.execute("CREATE INDEX IF NOT EXISTS idx_contacts_created_at ON contacts(created_at)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_contacts_email ON contacts(email)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_contacts_topic ON contacts(topic)")
    conn.commit()


def require_admin(credentials: HTTPBasicCredentials = Depends(security)) -> None:
    if not settings.admin_user or not settings.admin_password:
        raise HTTPException(status_code=503, detail="admin_not_configured")

    username_ok = secrets.compare_digest(credentials.username, settings.admin_user)
    password_ok = secrets.compare_digest(credentials.password, settings.admin_password)

    if not (username_ok and password_ok):
        raise HTTPException(
            status_code=401,
            detail="unauthorized",
            headers={"WWW-Authenticate": "Basic"},
        )


settings = load_settings()
conn = _connect(settings.db_path)
_init_db(conn)

app = FastAPI(title="da-tica portal API", version="1.0.0")


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/api/contacts", response_model=CreateContactResponse)
def create_contact(payload: CreateContactRequest) -> CreateContactResponse:
    created_at = datetime.now(tz=timezone.utc).isoformat()

    with _db_lock:
        try:
            cursor = conn.execute(
                """
                INSERT INTO contacts (created_at, name, email, subject, topic, message)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    created_at,
                    payload.name.strip(),
                    str(payload.email).strip().lower(),
                    payload.subject.strip(),
                    payload.topic,
                    payload.message.strip(),
                ),
            )
            conn.commit()
        except sqlite3.Error as exc:
            raise HTTPException(status_code=500, detail="db_error") from exc

    if cursor.lastrowid is None:
        raise HTTPException(status_code=500, detail="db_error")

    return CreateContactResponse(id=int(cursor.lastrowid), created_at=created_at)


@app.get("/api/admin/contacts", response_model=ListContactsResponse)
def list_contacts(
    limit: int = 100,
    offset: int = 0,
    topic: Topic | None = None,
    email: str | None = None,
    q: str | None = None,
    _: None = Depends(require_admin),
) -> ListContactsResponse:
    if limit < 1 or limit > 500:
        raise HTTPException(status_code=400, detail="invalid_limit")

    if offset < 0:
        raise HTTPException(status_code=400, detail="invalid_offset")

    where: list[str] = []
    params: list[object] = []

    if topic is not None:
        where.append("topic = ?")
        params.append(topic)

    if email is not None and email.strip():
        where.append("email = ?")
        params.append(email.strip().lower())

    if q is not None and q.strip():
        where.append("(subject LIKE ? OR message LIKE ?)")
        like = f"%{q.strip()}%"
        params.extend([like, like])

    where_sql = (" WHERE " + " AND ".join(where)) if where else ""

    sql = (
        "SELECT id, created_at, name, email, subject, topic, message "
        "FROM contacts" + where_sql + " ORDER BY id DESC LIMIT ? OFFSET ?"
    )

    params.extend([limit, offset])

    with _db_lock:
        rows = conn.execute(sql, params).fetchall()

    items = [
        Contact(
            id=int(r["id"]),
            created_at=str(r["created_at"]),
            name=str(r["name"]),
            email=str(r["email"]),
            subject=str(r["subject"]),
            topic=str(r["topic"]),
            message=str(r["message"]),
        )
        for r in rows
    ]

    return ListContactsResponse(items=items)
