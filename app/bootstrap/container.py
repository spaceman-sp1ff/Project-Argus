from app.engine.argus import Argus
from app.repositories.json_conversation_repository import (
    JsonConversationRepository,
)
from app.runtime.argus_runtime import ArgusRuntime
from app.services.context_builder import ContextBuilder


class ArgusContainer:
    """Constructs and connects Project Argus application components."""

    def create_runtime(self) -> ArgusRuntime:
        """Create a fully configured Argus Runtime."""

        engine = Argus()
        context_builder = ContextBuilder()
        conversation_repository = JsonConversationRepository()

        return ArgusRuntime(
            engine=engine,
            context_builder=context_builder,
            conversation_repository=conversation_repository,
        )