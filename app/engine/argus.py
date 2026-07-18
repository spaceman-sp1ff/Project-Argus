from collections.abc import Sequence

from app.models.conversation import Message
from app.providers.base import AIProvider
from app.providers.factory import ProviderFactory


class Argus:
    """Executes AI workloads through the configured provider."""

    def __init__(
        self,
        provider: AIProvider | None = None,
    ) -> None:
        self.provider = provider or ProviderFactory.create()

    @property
    def provider_name(self) -> str:
        """Return the configured provider's name."""

        return self.provider.__class__.__name__

    def execute(
        self,
        context: Sequence[Message],
    ) -> str:
        """Execute the supplied context through the AI provider."""

        return self.provider.generate_response(context)