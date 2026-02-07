from __future__ import annotations

import os
import sqlite3
import threading
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Literal

from fastapi import FastAPI, HTTPException
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


@dataclass(frozen=True)
class Settings:
    db_path: str


def load_settings() -> Settings:
    return Settings(db_path=os.environ.get("DB_PATH", "/data/contacts.db"))


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
    conn.commit()


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
