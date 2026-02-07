# SKILL: Manage Antigravity Configuration (Self-Install MCPs)

This skill allows the AI Agent to modify its own Antigravity IDE configuration to install, update, or remove MCP servers.

## SERVER CONTEXT
- **Target File:** `C:\Users\{USER_NAME}\.gemini\antigravity\mcp_config.json`
- **Format:** JSON matching the MCP Server standard.

## CAPABILITIES
1. **Locate Config:** Dynamically find the `mcp_config.json` file.
2. **Read Config:** Safely parse the existing JSON configuration.
3. **Install MCP:** Append a new server entry to the `mcpServers` object.
4. **Update/Remove:** Modify or delete existing server entries.

## PROTOCOL FOR INSTALLATION
When a user asks to "install an MCP", the agent SHOULD:
1. Identify the name of the MCP server and the necessary command/arguments (e.g., `npx -y @modelcontextprotocol/server-notebooklm`).
2. Read the current `mcp_config.json`.
3. Create a backup of the configuration within the same folder as `mcp_config.json.bak`.
4. Update the JSON content with the new server entry.
5. Write the modified content back to the file.
6. Notify the user that the IDE may need a refresh or restart to detect the new tools.

## SECURITY WARNING
- Never delete the entire `mcpServers` object.
- Always ensure valid JSON syntax to avoid breaking the agent's tools.
- Verify that the command is from a trusted source.

## EXAMPLE: NotebookLM Installation
```json
{
  "mcpServers": {
    "notebooklm": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-notebooklm"]
    }
  }
}
```
