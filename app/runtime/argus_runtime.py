from app.engine.argus import Argus
from app.repositories.conversation_repository import ConversationRepository
from app.services.context_builder import ContextBuilder


class ArgusRuntime:
    """Coordinates the lifecycle of an Argus conversation session."""

    def __init__(
        self,
        engine: Argus,
        context_builder: ContextBuilder,
        conversation_repository: ConversationRepository,
    ) -> None:
        self._engine = engine
        self._context_builder = context_builder
        self._conversation_repository = conversation_repository