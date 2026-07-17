import ollama

from app.core.config import settings
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

    def generate_response(self, prompt: str) -> str:
        """Send a prompt to a local Ollama model and return its response."""

        if not prompt.strip():
            raise ProviderRequestError("Prompt cannot be empty.")

        try:
            response = self.client.generate(
                model=self.model,
                prompt=prompt,
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

        text = response.response.strip()

        if not text:
            raise ProviderRequestError(
                "Ollama returned an empty response."
            )

        return text
