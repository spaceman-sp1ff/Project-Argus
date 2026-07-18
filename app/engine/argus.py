from app.models.chat import ChatRequest, ChatResponse
from app.models.conversation import Conversation
from app.providers.base import AIProvider
from app.providers.factory import ProviderFactory


class Argus:
    """Central orchestration engine for Project Argus."""

    def __init__(
        self,
        provider: AIProvider | None = None,
        conversation: Conversation | None = None,
    ) -> None:
        self.provider = provider or ProviderFactory.create()
        self.conversation = conversation or Conversation()

    def chat(self, request: ChatRequest) -> ChatResponse:
        """Process a chat request through the configured AI provider."""
        prompt = request.cleaned_prompt()

        if not prompt:
            raise ValueError("Prompt cannot be empty.")

        self.conversation.add_user_message(prompt)

        content = self.provider.generate_response(
            self.conversation.history()
        )

        self.conversation.add_assistant_message(content)

        return ChatResponse(
            content=content,
            provider=self.provider.__class__.__name__,
            metadata={
                **request.metadata,
                "conversation_id": str(self.conversation.id),
                "message_count": len(self.conversation.messages),
            },
        )