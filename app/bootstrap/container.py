from pathlib import Path

from app.engine.argus import Argus
from app.repositories.json_conversation_repository import (
    JsonConversationRepository,
)
from app.repositories.json_memory_repository import JsonMemoryRepository
from app.runtime.argus_runtime import ArgusRuntime
from app.services.context_builder import ContextBuilder
from app.services.memory_service import MemoryService


class ArgusContainer:
    """Constructs, owns, and provides Project Argus application components."""

    def __init__(self) -> None:
        self._runtime: ArgusRuntime | None = None
        self._memory_repository: JsonMemoryRepository | None = None
        self._memory_service: MemoryService | None = None

    def runtime(self) -> ArgusRuntime:
        """Return the application runtime, creating it when first requested."""

        if self._runtime is None:
            self._runtime = self._build_runtime()

        return self._runtime

    def memory_repository(self) -> JsonMemoryRepository:
        """Return the memory repository, creating it when first requested."""

        if self._memory_repository is None:
            self._memory_repository = JsonMemoryRepository(
                file_path=Path("data/memories.json"),
            )

        return self._memory_repository

    def memory_service(self) -> MemoryService:
        """Return the memory service, creating it when first requested."""

        if self._memory_service is None:
            self._memory_service = MemoryService(
                repository=self.memory_repository(),
            )

        return self._memory_service

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