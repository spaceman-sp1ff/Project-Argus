from app.engine.argus import Argus
from app.models.chat import ChatRequest
from app.providers.exceptions import ProviderError


def main() -> None:
    argus = Argus()

    requests = [
        ChatRequest(
            prompt="My name is Matt.",
            metadata={"source": "command_line"},
        ),
        ChatRequest(
            prompt="What name did I just tell you?",
            metadata={"source": "command_line"},
        ),
    ]

    try:
        for request in requests:
            response = argus.chat(request)

            print("\n=== ARGUS RESPONSE ===\n")
            print(response.content)
            print(f"\nProvider: {response.provider}")
            print(
                f"Conversation ID: "
                f"{response.metadata['conversation_id']}"
            )
            print(
                f"Messages: "
                f"{response.metadata['message_count']}"
            )

    except ProviderError as exc:
        print(f"Argus provider error: {exc}")
    except ValueError as exc:
        print(f"Argus input error: {exc}")


if __name__ == "__main__":
    main()
