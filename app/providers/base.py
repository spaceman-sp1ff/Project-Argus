from abc import ABC, abstractmethod


class AIProvider(ABC):
    """Base contract for every AI model provider used by Project Argus."""

    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        """Send a prompt to the provider and return its text response."""
        raise NotImplementedError
