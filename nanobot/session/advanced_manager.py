"""Advanced session management using inheritance."""

import json
from pathlib import Path
from typing import Any

from loguru import logger

from nanobot.session.manager import Session, SessionManager
from nanobot.utils.helpers import ensure_dir, safe_filename


class AdvancedSessionManager(SessionManager):
    """
    Advanced session manager that supports named sessions.
    Inherits from the base SessionManager to avoid modifying core files.
    """

    def __init__(self, workspace: Path):
        super().__init__(workspace)
        self.active_sessions_file = self.workspace / "active_sessions.json"
        self._active_sessions_cache: dict[str, str] = self._load_active_sessions()

    def _load_active_sessions(self) -> dict[str, str]:
        """Load the mapping of user -> active session name."""
        if not self.active_sessions_file.exists():
            return {}
        try:
            with open(self.active_sessions_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Failed to load active sessions: {e}")
            return {}

    def _save_active_sessions(self) -> None:
        """Save the mapping of user -> active session name."""
        try:
            with open(self.active_sessions_file, "w", encoding="utf-8") as f:
                json.dump(self._active_sessions_cache, f, indent=2)
        except Exception as e:
            logger.error(f"Failed to save active sessions: {e}")

    def get_active_session_name(self, user_key: str) -> str:
        """Get the currently active session name for a user."""
        return self._active_sessions_cache.get(user_key, "default")

    def set_active_session(self, user_key: str, session_name: str) -> None:
        """Set the active session for a user."""
        if session_name == "default":
            self._active_sessions_cache.pop(user_key, None)
        else:
            self._active_sessions_cache[user_key] = session_name
        self._save_active_sessions()

    def _get_full_key(self, user_key: str, session_name: str = None) -> str:
        """Generate the full storage key combining user and session name."""
        name = session_name or self.get_active_session_name(user_key)
        if name == "default":
            return user_key
        return f"{user_key}::{name}"

    def get_or_create(self, key: str) -> Session:
        """
        Override get_or_create to inject the active session name.
        The 'key' passed here is usually 'channel:chat_id'.
        """
        full_key = self._get_full_key(key)
        return super().get_or_create(full_key)

    def get_user_sessions(self, user_key: str) -> list[dict[str, Any]]:
        """List all sessions belonging to a specific user."""
        all_sessions = self.list_sessions()
        user_sessions = []
        
        for s in all_sessions:
            s_key = s.get("key", "")
            if s_key == user_key:
                s["name"] = "default"
                user_sessions.append(s)
            elif s_key.startswith(f"{user_key}::"):
                s["name"] = s_key.split("::", 1)[1]
                user_sessions.append(s)
                
        return user_sessions
