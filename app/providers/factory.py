from app.core.config import settings
from app.providers.base import AIProvider
from app.providers.exceptions import ProviderConfigurationError
from app.providers.ollama_provider import OllamaProvider
from app.providers.openai_provider import OpenAIProvider


class ProviderFactory:
    """Create the configured AI provider."""

    @staticmethod
    def create() -> AIProvider:
        provider_name = settings.ai_provider.strip().lower()

        if provider_name == "ollama":
            return OllamaProvider()

        if provider_name == "openai":
            return OpenAIProvider()

        raise ProviderConfigurationError(
            f"Unsupported AI provider: {settings.ai_provider}"
        )
