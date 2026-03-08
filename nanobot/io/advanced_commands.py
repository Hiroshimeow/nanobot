import os
from typing import Optional, List
from nanobot.session.advanced_manager import AdvancedSessionManager
from nanobot.bus.events import InboundMessage, OutboundMessage

class AdvancedCommandHandler:
    """
    Handles advanced session commands: /session, /list, /new.
    Integrated into AgentLoop.
    """
    def __init__(self, session_manager: AdvancedSessionManager, bus=None):
        self.session_manager = session_manager
        self.bus = bus

    async def handle_command(self, msg: InboundMessage) -> bool:
        """
        Process advanced session commands from an InboundMessage.
        Returns True if the command was handled, else False.
        """
        from loguru import logger
        content = msg.content.strip()
        if not content.startswith("/"):
            return False

        parts = content[1:].split()
        if not parts:
            return False
        
        command = parts[0].lower()
        args = parts[1:]
        
        logger.info(f"AdvancedCommandHandler: Received command /{command} with args {args}")

        response_text = None

        if command == "session":
            if not args:
                current = self.session_manager.current_session_name
                response_text = f"Current session: **{current}**\nUse `/session [name]` to switch."
            else:
                name = args[0]
                session_id = self.session_manager.switch_session(name)
                if session_id:
                    response_text = f"Switched to session: **{name}** (ID: {session_id})"
                else:
                    response_text = f"Session **{name}** not found. Use `/new {name}` to create it."

        elif command == "list":
            sessions = self.session_manager.list_sessions()
            current = self.session_manager.current_session_name
            session_list = "\n".join([f"- {s} {'(active)' if s == current else ''}" for s in sessions])
            response_text = f"Available sessions:\n{session_list}"

        elif command == "new" and len(args) > 0:
            # Only handle /new if it has arguments (named session)
            # Standard /new is handled by the core loop
            name = args[0]
            session_id = self.session_manager.create_session(name)
            self.session_manager.switch_session(name)
            response_text = f"Created and switched to new session: **{name}** (ID: {session_id})"

        if response_text and self.bus:
            await self.bus.publish_outbound(
                OutboundMessage(
                    channel=msg.channel,
                    chat_id=msg.chat_id,
                    content=response_text
                )
            )
            return True

        return False
