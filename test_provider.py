from app.providers.exceptions import ProviderError
from app.providers.factory import ProviderFactory


def main() -> None:
    try:
        provider = ProviderFactory.create()

        response = provider.generate_response(
            "In one sentence, introduce yourself as Project Argus."
        )
    except ProviderError as exc:
        print(f"Argus provider error: {exc}")
        return

    print("\n=== ARGUS RESPONSE ===\n")
    print(response)


if __name__ == "__main__":
    main()
