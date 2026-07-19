from app.bootstrap import ArgusContainer
from app.models.chat import ChatRequest


def main() -> None:
    container = ArgusContainer()
    runtime = container.create_runtime()

    conversation = runtime.start_conversation()

    requests = [
        ChatRequest(prompt="My name is Matt."),
        ChatRequest(prompt="What name did I just tell you?"),
    ]

    for request in requests:
        response = runtime.chat(
            conversation=conversation,
            request=request,
        )

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