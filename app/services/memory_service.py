from collections.abc import Mapping

from app.models.memory import Memory
from app.repositories.memory_repository import MemoryRepository


class MemoryService:
    """
    Application service for managing long-term memories.

    The service owns memory-related application behavior while delegating
    persistence to a MemoryRepository implementation.
    """

    def __init__(self, repository: MemoryRepository) -> None:
        self._repository = repository

    def remember(
        self,
        content: str,
        source: str,
        importance: float = 0.5,
        metadata: Mapping[str, str] | None = None,
    ) -> Memory:
        """
        Create and persist a new memory.

        Returns the stored Memory so callers can access its generated ID
        and creation timestamp.
        """
        memory = Memory(
            content=content,
            source=source,
            importance=importance,
            metadata=metadata or {},
        )

        self._repository.save(memory)

        return memory

    def get(self, memory_id: str) -> Memory | None:
        """
        Retrieve a memory by its unique ID.
        """
        return self._repository.get(memory_id)

    def all(self) -> list[Memory]:
        """
        Return every stored memory.
        """
        return self._repository.list_all()

    def forget(self, memory_id: str) -> bool:
        """
        Delete a memory by its unique ID.

        Returns True when a memory was deleted.
        """
        return self._repository.delete(memory_id)