from collections.abc import Sequence

from app.core.constants import ARGUS_SYSTEM_PROMPT
from app.models.conversation import (
    Conversation,
    Message,
    MessageRole,
)


class ContextBuilder:
    """Builds the conversation context supplied to AI providers."""

    def _system_message(self) -> Message:
        """Create the default Argus system message."""

        return Message(
            role=MessageRole.SYSTEM,
            content=ARGUS_SYSTEM_PROMPT,
        )

    def build(
        self,
        conversation: Conversation,
    ) -> Sequence[Message]:
        """Construct the ordered context for an AI provider."""

        history = conversation.history()

        if not history:
            raise ValueError(
                "Conversation history cannot be empty."
            )

        return (
            self._system_message(),
            *history,
        )