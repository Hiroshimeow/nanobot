"""Advanced commands for session management."""

from typing import Any

from loguru import logger

from nanobot.bus.events import InboundMessage, OutboundMessage
from nanobot.session.advanced_manager import AdvancedSessionManager


class AdvancedCommandHandler:
    """
    Handles advanced commands like /session, /list, /new.
    Intercepts messages before they reach the LLM.
    """

    def __init__(self, session_manager: AdvancedSessionManager, bus: Any):
        self.session_manager = session_manager
        self.bus = bus

    async def handle_command(self, msg: InboundMessage) -> bool:
        """
        Process a command. Returns True if handled, False otherwise.
        """
        text = msg.content.strip()
        if not text.startswith("/"):
            return False

        parts = text.split()
        cmd = parts[0].lower()
        args = parts[1:]
        user_key = f"{msg.channel}:{msg.chat_id}"

        if cmd == "/session":
            if not args:
                active = self.session_manager.get_active_session_name(user_key)
                await self._send_reply(msg, f"You are currently in session: `{active}`")
                return True
            
            subcmd = args[0].lower()
            if subcmd == "list":
                await self._handle_list(msg, user_key)
            else:
                session_name = args[0]
                self.session_manager.set_active_session(user_key, session_name)
                await self._send_reply(msg, f"Switched to session: `{session_name}`")
            return True

        elif cmd == "/list":
            await self._handle_list(msg, user_key)
            return True

        elif cmd == "/new":
            session_name = args[0] if args else "default"
            
            if session_name == "default":
                # Clear default session
                session = self.session_manager.get_or_create(user_key)
                session.clear()
                self.session_manager.save(session)
                self.session_manager.set_active_session(user_key, "default")
                await self._send_reply(msg, "Default session cleared and activated.")
            else:
                # Create/switch to new named session
                self.session_manager.set_active_session(user_key, session_name)
                full_key = f"{user_key}::{session_name}"
                session = self.session_manager.get_or_create(full_key)
                session.clear()
                self.session_manager.save(session)
                await self._send_reply(msg, f"Created and switched to new session: `{session_name}`")
            return True

        return False

    async def _handle_list(self, msg: InboundMessage, user_key: str) -> None:
        """Handle the /list command."""
        sessions = self.session_manager.get_user_sessions(user_key)
        active = self.session_manager.get_active_session_name(user_key)
        
        if not sessions:
            await self._send_reply(msg, "No sessions found.")
            return

        lines = ["**Your Sessions:**"]
        for s in sessions:
            name = s.get("name", "unknown")
            mark = " (active)" if name == active else ""
            lines.append(f"- `{name}`{mark}")
            
        await self._send_reply(msg, "\n".join(lines))

    async def _send_reply(self, msg: InboundMessage, content: str) -> None:
        """Send a reply back to the user."""
        out = OutboundMessage(
            channel=msg.channel,
            chat_id=msg.chat_id,
            content=content,
            reply_to_message_id=msg.message_id,
        )
        await self.bus.publish_outbound(out)
