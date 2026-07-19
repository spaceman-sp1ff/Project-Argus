import json
from datetime import datetime
from pathlib import Path
from typing import Any

from app.models.memory import Memory


class JsonMemoryRepository:
    """
    JSON-backed implementation of the MemoryRepository contract.

    This repository is responsible only for serializing, persisting,
    loading, and deleting Memory objects.
    """

    def __init__(self, file_path: Path) -> None:
        self._file_path = file_path

    def save(self, memory: Memory) -> None:
        memories = self.list_all()

        updated_memories = [
            existing_memory
            for existing_memory in memories
            if existing_memory.id != memory.id
        ]

        updated_memories.append(memory)

        self._write_memories(updated_memories)

    def get(self, memory_id: str) -> Memory | None:
        for memory in self.list_all():
            if memory.id == memory_id:
                return memory

        return None

    def list_all(self) -> list[Memory]:
        if not self._file_path.exists():
            return []

        try:
            raw_data = self._file_path.read_text(encoding="utf-8")
        except OSError as error:
            raise RuntimeError(
                f"Unable to read memory file: {self._file_path}"
            ) from error

        if not raw_data.strip():
            return []

        try:
            stored_memories = json.loads(raw_data)
        except json.JSONDecodeError as error:
            raise RuntimeError(
                f"Memory file contains invalid JSON: {self._file_path}"
            ) from error

        if not isinstance(stored_memories, list):
            raise RuntimeError(
                f"Memory file must contain a JSON list: {self._file_path}"
            )

        return [
            self._deserialize_memory(memory_data)
            for memory_data in stored_memories
        ]

    def delete(self, memory_id: str) -> bool:
        memories = self.list_all()

        remaining_memories = [
            memory
            for memory in memories
            if memory.id != memory_id
        ]

        if len(remaining_memories) == len(memories):
            return False

        self._write_memories(remaining_memories)

        return True

    def _write_memories(self, memories: list[Memory]) -> None:
        self._file_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        serialized_memories = [
            self._serialize_memory(memory)
            for memory in memories
        ]

        try:
            self._file_path.write_text(
                json.dumps(
                    serialized_memories,
                    indent=2,
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
        except OSError as error:
            raise RuntimeError(
                f"Unable to write memory file: {self._file_path}"
            ) from error

    @staticmethod
    def _serialize_memory(memory: Memory) -> dict[str, Any]:
        return {
            "id": memory.id,
            "content": memory.content,
            "source": memory.source,
            "created_at": memory.created_at.isoformat(),
            "importance": memory.importance,
            "metadata": dict(memory.metadata),
        }

    @staticmethod
    def _deserialize_memory(data: Any) -> Memory:
        if not isinstance(data, dict):
            raise RuntimeError(
                "Each stored memory must be a JSON object."
            )

        try:
            return Memory(
                id=str(data["id"]),
                content=str(data["content"]),
                source=str(data["source"]),
                created_at=datetime.fromisoformat(
                    str(data["created_at"])
                ),
                importance=float(data.get("importance", 0.5)),
                metadata={
                    str(key): str(value)
                    for key, value in data.get(
                        "metadata",
                        {},
                    ).items()
                },
            )
        except (
            KeyError,
            TypeError,
            ValueError,
            AttributeError,
        ) as error:
            raise RuntimeError(
                "Stored memory contains invalid data."
            ) from error