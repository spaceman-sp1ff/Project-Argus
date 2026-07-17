class ProviderError(Exception):
    """Base exception for AI provider failures."""


class ProviderAuthenticationError(ProviderError):
    """Raised when provider credentials are missing or invalid."""


class ProviderQuotaError(ProviderError):
    """Raised when a provider account has no available quota."""


class ProviderConnectionError(ProviderError):
    """Raised when the provider cannot be reached."""


class ProviderConfigurationError(ProviderError):
    """Raised when a provider or model is configured incorrectly."""


class ProviderRequestError(ProviderError):
    """Raised when a provider rejects a request."""
