from abc import ABC, abstractmethod

from app.models.conversation import Conversation


class ConversationRepository(ABC):
    """Persistence contract for conversation storage."""

    @abstractmethod
    def save(
        self,
        conversation: Conversation,
    ) -> None:
        """Persist a conversation."""
        raise NotImplementedError

    @abstractmethod
    def load(
        self,
        conversation_id: str,
    ) -> Conversation:
        """Load a conversation by its ID."""
        raise NotImplementedError