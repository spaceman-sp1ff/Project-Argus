from app.engine.argus import Argus
from app.models.chat import ChatRequest


def main() -> None:
    argus = Argus()

    requests = [
        ChatRequest(prompt="My name is Matt."),
        ChatRequest(prompt="What name did I just tell you?"),
    ]

    for request in requests:
        response = argus.chat(request)

        print("\n=== ARGUS RESPONSE ===\n")
        print(response.content)
        print()
        print(f"Provider: {response.provider}")
        print(
            f"Conversation ID: "
            f"{response.metadata['conversation_id']}"
        )
        print(
            f"Messages: "
            f"{response.metadata['message_count']}"
        )


if __name__ == "__main__":
    main()