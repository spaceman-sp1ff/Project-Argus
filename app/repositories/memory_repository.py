from typing import Protocol

from app.models.memory import Memory


class MemoryRepository(Protocol):
    """
    Persistence contract for long-term memories.

    Repository implementations are responsible only for storing and
    retrieving Memory objects. They do not decide what should be remembered
    or which memories are relevant to a request.
    """

    def save(self, memory: Memory) -> None:
        """
        Store a new memory or replace an existing memory with the same ID.
        """
        ...

    def get(self, memory_id: str) -> Memory | None:
        """
        Retrieve a memory by its unique ID.

        Returns None when no matching memory exists.
        """
        ...

    def list_all(self) -> list[Memory]:
        """
        Return every stored memory.
        """
        ...

    def delete(self, memory_id: str) -> bool:
        """
        Delete a memory by its unique ID.

        Returns True when a memory was deleted and False when no matching
        memory existed.
        """
        ...
