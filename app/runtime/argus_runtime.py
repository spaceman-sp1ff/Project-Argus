from uuid import UUID

from app.engine.argus import Argus
from app.models.chat import ChatRequest, ChatResponse
from app.models.conversation import Conversation
from app.repositories.conversation_repository import (
    ConversationRepository,
)
from app.services.context_builder import ContextBuilder
from app.services.memory_service import MemoryService


class ArgusRuntime:
    """Coordinates the lifecycle of an Argus conversation session."""

    def __init__(
        self,
        engine: Argus,
        context_builder: ContextBuilder,
        conversation_repository: ConversationRepository,
        memory_service: MemoryService,
    ) -> None:
        self._engine = engine
        self._context_builder = context_builder
        self._conversation_repository = conversation_repository
        self._memory_service = memory_service

    def start_conversation(self) -> Conversation:
        """Create and return a new conversation."""

        return Conversation()

    def load_conversation(
        self,
        conversation_id: UUID,
    ) -> Conversation:
        """Restore an existing conversation from persistence."""

        return self._conversation_repository.load(conversation_id)

    def chat(
        self,
        conversation: Conversation,
        request: ChatRequest,
    ) -> ChatResponse:
        """Process a single conversational turn."""

        prompt = request.cleaned_prompt()

        if not prompt:
            raise ValueError("Prompt cannot be empty.")

        conversation.add_user_message(prompt)

        context = self._context_builder.build(conversation)

        content = self._engine.execute(context)

        conversation.add_assistant_message(content)

        self._conversation_repository.save(conversation)

        return ChatResponse(
            content=content,
            provider=self._engine.provider_name,
            metadata={
                **request.metadata,
                "conversation_id": str(conversation.id),
                "message_count": len(conversation.messages),
            },
        )