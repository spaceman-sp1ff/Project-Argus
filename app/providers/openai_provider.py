from collections.abc import Sequence

import openai
from openai import OpenAI

from app.core.config import settings
from app.models.conversation import Message, MessageRole
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
            response = self.client.responses.create(
                model=self.model,
                input=serialized_messages,
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

        text = response.output_text.strip()

        if not text:
            raise ProviderRequestError(
                "OpenAI returned an empty response."
            )

        return text

    @staticmethod
    def _serialize_message(message: Message) -> dict[str, str]:
        """Convert an Argus message into OpenAI's input format."""

        if message.role is MessageRole.TOOL:
            raise ProviderRequestError(
                "Tool messages are not supported yet."
            )

        return {
            "role": message.role.value,
            "content": message.content,
        }

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
