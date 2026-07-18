from app.models.conversation import Conversation
from app.repositories.conversation_repository import (
    ConversationRepository,
)


class JsonConversationRepository(
    ConversationRepository
):
    """JSON-backed conversation repository."""

    def save(
        self,
        conversation: Conversation,
    ) -> None:
        raise NotImplementedError(
            "JSON persistence has not been implemented yet."
        )

    def load(
        self,
        conversation_id: str,
    ) -> Conversation:
        raise NotImplementedError(
            "JSON persistence has not been implemented yet."
        )