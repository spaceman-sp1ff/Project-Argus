from app.engine.argus import Argus
from app.models.chat import ChatRequest
from app.repositories.json_conversation_repository import (
    JsonConversationRepository,
)
from app.runtime.argus_runtime import ArgusRuntime
from app.services.context_builder import ContextBuilder


def main() -> None:
    engine = Argus()
    context_builder = ContextBuilder()
    conversation_repository = JsonConversationRepository()

    runtime = ArgusRuntime(
        engine=engine,
        context_builder=context_builder,
        conversation_repository=conversation_repository,
    )

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