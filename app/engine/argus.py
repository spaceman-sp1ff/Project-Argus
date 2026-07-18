from app.models.chat import ChatRequest, ChatResponse
from app.models.conversation import Conversation
from app.providers.base import AIProvider
from app.providers.factory import ProviderFactory
from app.services.context_builder import ContextBuilder


class Argus:
    """Central orchestration engine for Project Argus."""

    def __init__(
        self,
        provider: AIProvider | None = None,
        conversation: Conversation | None = None,
        context_builder: ContextBuilder | None = None,
    ) -> None:
        self.provider = provider or ProviderFactory.create()
        self.conversation = conversation or Conversation()
        self.context_builder = context_builder or ContextBuilder()

    def chat(self, request: ChatRequest) -> ChatResponse:
        """Process a chat request through the configured AI provider."""

        prompt = request.cleaned_prompt()

        if not prompt:
            raise ValueError("Prompt cannot be empty.")

        # Store the user's message.
        self.conversation.add_user_message(prompt)

        # Build the context that will be sent to the provider.
        context = self.context_builder.build(
            self.conversation
        )

        # Generate the assistant response.
        content = self.provider.generate_response(
            context
        )

        # Store the assistant's response.
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