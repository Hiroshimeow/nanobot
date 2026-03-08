import json
import os
from pathlib import Path
from typing import List, Optional
from nanobot.session.manager import SessionManager

class AdvancedSessionManager(SessionManager):
    """
    Advanced Session Manager that supports named sessions and persistence.
    Inherits from SessionManager to maintain compatibility with core logic.
    """
    def __init__(self, workspace: str | Path):
        # Ensure workspace is a Path object for compatibility with SessionManager
        workspace_path = Path(workspace)
        super().__init__(workspace_path)
        self.sessions_file = workspace_path / "active_sessions.json"
        self.active_sessions = self._load_sessions()
        self.current_session_name = "default"

    def _load_sessions(self) -> dict:
        if self.sessions_file.exists():
            try:
                with open(self.sessions_file, "r") as f:
                    return json.load(f)
            except Exception:
                return {"default": "default"}
        return {"default": "default"}

    def _save_sessions(self):
        with open(self.sessions_file, "w") as f:
            json.dump(self.active_sessions, f, indent=4)

    def create_session(self, name: str) -> str:
        """Create a new named session."""
        session_id = f"session_{name}"
        self.active_sessions[name] = session_id
        self._save_sessions()
        # Ensure session directory exists
        session_path = self.workspace / "sessions" / session_id
        session_path.mkdir(parents=True, exist_ok=True)
        return session_id

    def list_sessions(self) -> List[str]:
        """List all available session names."""
        return list(self.active_sessions.keys())

    def switch_session(self, name: str) -> Optional[str]:
        """Switch to an existing named session."""
        if name in self.active_sessions:
            self.current_session_name = name
            return self.active_sessions[name]
        return None

    def get_current_session_id(self) -> str:
        """Get the ID of the currently active session."""
        return self.active_sessions.get(self.current_session_name, "default")
