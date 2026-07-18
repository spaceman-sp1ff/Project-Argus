import json
from datetime import datetime
from pathlib import Path
from uuid import UUID

from app.models.conversation import (
    Conversation,
    Message,
    MessageRole,
)
from app.repositories.conversation_repository import (
    ConversationRepository,
)


class JsonConversationRepository(
    ConversationRepository
):
    """JSON-backed conversation repository."""

    def __init__(
        self,
        directory: str = ".conversations",
    ) -> None:
        self.directory = Path(directory)
        self.directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    def save(
        self,
        conversation: Conversation,
    ) -> None:
        file_path = self.directory / f"{conversation.id}.json"

        data = {
            "id": str(conversation.id),
            "created_at": conversation.created_at.isoformat(),
            "messages": [
                {
                    "role": message.role.value,
                    "content": message.content,
                    "created_at": message.created_at.isoformat(),
                }
                for message in conversation.messages
            ],
        }

        with file_path.open(
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                data,
                file,
                indent=2,
                ensure_ascii=False,
            )

    def load(
        self,
        conversation_id: str,
    ) -> Conversation:
        file_path = self.directory / f"{conversation_id}.json"

        if not file_path.exists():
            raise FileNotFoundError(
                f"Conversation '{conversation_id}' was not found."
            )

        with file_path.open(
            "r",
            encoding="utf-8",
        ) as file:
            data = json.load(file)

        messages = [
            Message(
                role=MessageRole(message_data["role"]),
                content=message_data["content"],
                created_at=datetime.fromisoformat(
                    message_data["created_at"]
                ),
            )
            for message_data in data["messages"]
        ]

        return Conversation(
            id=UUID(data["id"]),
            messages=messages,
            created_at=datetime.fromisoformat(
                data["created_at"]
            ),
        )