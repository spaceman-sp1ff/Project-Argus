from collections.abc import Sequence

from app.models.conversation import Conversation, Message


class ContextBuilder:
    """Builds the conversation context supplied to AI providers."""

    def build(
        self,
        conversation: Conversation,
    ) -> Sequence[Message]:
        """
        Construct the ordered context for an AI provider.

        The ContextBuilder is responsible for deciding what information
        should be visible to the language model.

        For now, this is simply the conversation history.
        """

        history = conversation.history()

        if not history:
            raise ValueError(
                "Conversation history cannot be empty."
            )

        return history