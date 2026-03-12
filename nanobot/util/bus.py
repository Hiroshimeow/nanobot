from typing import Any, Callable, Coroutine, TypeVar


_MessageType = TypeVar("_MessageType")
_HandlerType = Callable[[_MessageType], Coroutine[Any, Any, None]]


class MessageBus:
    """A minimal message bus for inter-component communication."""

    def __init__(self):
        self._handlers: dict[type, list[_HandlerType]] = {}

    def subscribe(self, message_type: type[_MessageType], handler: _HandlerType) -> None:
        """Subscribe a handler to a message type."""
        if message_type not in self._handlers:
            self._handlers[message_type] = []
        self._handlers[message_type].append(handler)

    async def publish(self, message: _MessageType) -> None:
        """Publish a message to all subscribers."""
        message_type = type(message)
        if message_type in self._handlers:
            for handler in self._handlers[message_type]:
                await handler(message)
