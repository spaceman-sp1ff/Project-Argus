from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass(frozen=True)
class ChatRequest:
    """A request submitted to the Argus Engine."""

    prompt: str
    metadata: dict[str, Any] = field(default_factory=dict)

    def cleaned_prompt(self) -> str:
        """Return the prompt with surrounding whitespace removed."""
        return self.prompt.strip()


@dataclass(frozen=True)
class ChatResponse:
    """A response produced by the Argus Engine."""

    content: str
    provider: str
    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    metadata: dict[str, Any] = field(default_factory=dict)
