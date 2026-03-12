from nanobot.agent.tools.base import Tool
from nanobot.agent.tools.registry import ToolRegistry
from pathlib import Path
from typing import Any


class FileTool(Tool):
    """A tool for reading and writing files."""

    def __init__(self, tools: ToolRegistry, workspace: Path):
        self._tools = tools
        self._workspace = workspace

    @property
    def name(self) -> str:
        return "file"

    @property
    def description(self) -> str:
        return "Reads and writes files."

    @property
    def parameters(self) -> dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "description": "The action to perform (read or write).",
                    "enum": ["read", "write"],
                },
                "path": {
                    "type": "string",
                    "description": "The path to the file.",
                },
                "content": {
                    "type": "string",
                    "description": "The content to write to the file (only for write action).",
                },
            },
            "required": ["action", "path"],
        }

    async def execute(self, action: str, path: str, content: str | None = None) -> str:
        file_path = self._workspace / path

        if action == "read":
            return self._read_file(file_path)
        elif action == "write":
            if content is None:
                return "Error: Content is required for write action."
            return self._write_file(file_path, content)
        else:
            return f"Error: Unknown action '{action}' for file tool."

    def _read_file(self, path: Path) -> str:
        try:
            return path.read_text()
        except FileNotFoundError:
            return f"Error: File not found at {path}"
        except Exception as e:
            return f"Error reading file {path}: {e}"

    def _write_file(self, path: Path, content: str) -> str:
        try:
            path.write_text(content)
            return f"Successfully wrote to {path}"
        except Exception as e:
            return f"Error writing to file {path}: {e}"

    def set_context(self, *args, **kwargs):
        """Placeholder for context setting."""
        pass
