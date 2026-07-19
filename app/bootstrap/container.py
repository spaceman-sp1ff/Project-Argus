from app.engine.argus import Argus
from app.repositories.json_conversation_repository import (
    JsonConversationRepository,
)
from app.runtime.argus_runtime import ArgusRuntime
from app.services.context_builder import ContextBuilder


class ArgusContainer:
    """Constructs, owns, and provides Project Argus application components."""

    def __init__(self) -> None:
        self._runtime: ArgusRuntime | None = None

    def runtime(self) -> ArgusRuntime:
        """Return the application runtime, creating it when first requested."""

        if self._runtime is None:
            self._runtime = self._build_runtime()

        return self._runtime

    def _build_runtime(self) -> ArgusRuntime:
        """Construct a fully configured Argus Runtime."""

        engine = Argus()
        context_builder = ContextBuilder()
        conversation_repository = JsonConversationRepository()

        return ArgusRuntime(
            engine=engine,
            context_builder=context_builder,
            conversation_repository=conversation_repository,
        )