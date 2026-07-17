import openai
from openai import OpenAI

from app.core.config import settings
from app.providers.base import AIProvider
from app.providers.exceptions import (
    ProviderAuthenticationError,
    ProviderConfigurationError,
    ProviderConnectionError,
    ProviderQuotaError,
    ProviderRequestError,
)


class OpenAIProvider(AIProvider):
    """OpenAI implementation of the Project Argus AI provider contract."""

    def __init__(self) -> None:
        if not settings.openai_api_key:
            raise ProviderConfigurationError(
                "OPENAI_API_KEY is not configured."
            )

        if not settings.openai_model:
            raise ProviderConfigurationError(
                "OPENAI_MODEL is not configured."
            )

        self.client = OpenAI(api_key=settings.openai_api_key)
        self.model = settings.openai_model

    def generate_response(self, prompt: str) -> str:
        """Send a prompt to OpenAI and return the generated text."""

        if not prompt.strip():
            raise ProviderRequestError("Prompt cannot be empty.")

        try:
            response = self.client.responses.create(
                model=self.model,
                input=prompt,
            )
        except openai.AuthenticationError as exc:
            raise ProviderAuthenticationError(
                "OpenAI rejected the configured API key."
            ) from exc
        except openai.RateLimitError as exc:
            error_code = self._get_error_code(exc)

            if error_code == "insufficient_quota":
                raise ProviderQuotaError(
                    "OpenAI API quota is unavailable. Add API billing or use "
                    "a different provider."
                ) from exc

            raise ProviderRequestError(
                "OpenAI rate limit reached. Try again later."
            ) from exc
        except openai.APIConnectionError as exc:
            raise ProviderConnectionError(
                "Could not connect to the OpenAI API."
            ) from exc
        except openai.BadRequestError as exc:
            error_code = self._get_error_code(exc)

            if error_code == "model_not_found":
                raise ProviderConfigurationError(
                    f"The configured OpenAI model does not exist or is not "
                    f"available: {self.model}"
                ) from exc

            raise ProviderRequestError(
                f"OpenAI rejected the request: {exc.message}"
            ) from exc
        except openai.APIStatusError as exc:
            raise ProviderRequestError(
                f"OpenAI request failed with status {exc.status_code}."
            ) from exc

        return response.output_text

    @staticmethod
    def _get_error_code(exc: openai.APIStatusError) -> str | None:
        """Extract an OpenAI error code from an SDK exception body."""

        if isinstance(exc.body, dict):
            error = exc.body.get("error")

            if isinstance(error, dict):
                code = error.get("code")

                if isinstance(code, str):
                    return code

        return None
