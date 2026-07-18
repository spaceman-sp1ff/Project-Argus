from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from uuid import UUID, uuid4


class MessageRole(str, Enum):
    """Supported roles within an Argus conversation."""

    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"


@dataclass(frozen=True)
class Message:
    """A single message within a conversation."""

    role: MessageRole
    content: str
    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    def __post_init__(self) -> None:
        if not self.content.strip():
            raise ValueError("Message content cannot be empty.")


@dataclass
class Conversation:
    """Owns the ordered message history for an Argus session."""

    id: UUID = field(default_factory=uuid4)
    messages: list[Message] = field(default_factory=list)
    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    def add_message(self, role: MessageRole, content: str) -> Message:
        """Create and append a message to the conversation."""
        message = Message(
            role=role,
            content=content.strip(),
        )
        self.messages.append(message)
        return message

    def add_system_message(self, content: str) -> Message:
        return self.add_message(MessageRole.SYSTEM, content)

    def add_user_message(self, content: str) -> Message:
        return self.add_message(MessageRole.USER, content)

    def add_assistant_message(self, content: str) -> Message:
        return self.add_message(MessageRole.ASSISTANT, content)

    def add_tool_message(self, content: str) -> Message:
        return self.add_message(MessageRole.TOOL, content)

    def history(self) -> tuple[Message, ...]:
        """Return an immutable view of the conversation history."""
        return tuple(self.messages)

    def clear(self) -> None:
        """Remove every message from the conversation."""
        self.messages.clear()
