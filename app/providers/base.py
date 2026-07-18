from abc import ABC, abstractmethod
from collections.abc import Sequence

from app.models.conversation import Message


class AIProvider(ABC):
    """Base contract for every AI model provider used by Project Argus."""

    @abstractmethod
    def generate_response(self, messages: Sequence[Message]) -> str:
        """Generate a response using an ordered conversation history."""
        raise NotImplementedError
