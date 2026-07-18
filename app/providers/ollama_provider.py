from collections.abc import Sequence

import ollama

from app.core.config import settings
from app.models.conversation import Message, MessageRole
from app.providers.base import AIProvider
from app.providers.exceptions import (
    ProviderConfigurationError,
    ProviderConnectionError,
    ProviderRequestError,
)


class OllamaProvider(AIProvider):
    """Local Ollama implementation of the Argus provider contract."""

    def __init__(self) -> None:
        if not settings.ollama_model:
            raise ProviderConfigurationError(
                "OLLAMA_MODEL is not configured."
            )

        if not settings.ollama_host:
            raise ProviderConfigurationError(
                "OLLAMA_HOST is not configured."
            )

        self.model = settings.ollama_model
        self.client = ollama.Client(host=settings.ollama_host)

    def generate_response(self, messages: Sequence[Message]) -> str:
        """Generate a response using the supplied conversation history."""

        if not messages:
            raise ProviderRequestError(
                "Conversation history cannot be empty."
            )

        serialized_messages = [
            self._serialize_message(message)
            for message in messages
        ]

        try:
            response = self.client.chat(
                model=self.model,
                messages=serialized_messages,
            )
        except ConnectionError as exc:
            raise ProviderConnectionError(
                "Could not connect to the local Ollama service."
            ) from exc
        except ollama.ResponseError as exc:
            if exc.status_code == 404:
                raise ProviderConfigurationError(
                    f"The configured Ollama model is unavailable: {self.model}"
                ) from exc

            raise ProviderRequestError(
                f"Ollama rejected the request: {exc.error}"
            ) from exc

        text = response.message.content.strip()

        if not text:
            raise ProviderRequestError(
                "Ollama returned an empty response."
            )

        return text

    @staticmethod
    def _serialize_message(message: Message) -> dict[str, str]:
        """Convert an Argus message into Ollama's chat message format."""

        if message.role is MessageRole.TOOL:
            raise ProviderRequestError(
                "Tool messages are not supported yet."
            )

        return {
            "role": message.role.value,
            "content": message.content,
        }