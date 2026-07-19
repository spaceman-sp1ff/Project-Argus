from dataclasses import dataclass, field
from datetime import datetime, timezone
from types import MappingProxyType
from typing import Mapping
from uuid import uuid4


@dataclass(frozen=True)
class Memory:
    """
    A single long-term fact retained by Argus.

    A Memory represents distilled knowledge, not a raw conversation
    transcript.
    """

    content: str
    source: str
    importance: float = 0.5
    metadata: Mapping[str, str] = field(default_factory=dict)
    id: str = field(default_factory=lambda: str(uuid4()))
    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    def __post_init__(self) -> None:
        content = self.content.strip()
        source = self.source.strip()

        if not content:
            raise ValueError("Memory content cannot be empty.")

        if not source:
            raise ValueError("Memory source cannot be empty.")

        if not 0.0 <= self.importance <= 1.0:
            raise ValueError(
                "Memory importance must be between 0.0 and 1.0."
            )

        normalized_metadata = {
            str(key): str(value)
            for key, value in self.metadata.items()
        }

        object.__setattr__(self, "content", content)
        object.__setattr__(self, "source", source)
        object.__setattr__(
            self,
            "metadata",
            MappingProxyType(normalized_metadata),
        )