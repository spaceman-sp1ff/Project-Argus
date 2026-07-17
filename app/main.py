from rich.console import Console

from config import settings


console = Console()


def main() -> None:
    console.print("[bold green]Project Argus is online.[/bold green]")
    console.print(f"Environment: {settings.app_env}")
    console.print(f"AI model: {settings.openai_model}")

    if settings.openai_api_key:
        console.print("[green]API key detected.[/green]")
    else:
        console.print("[yellow]API key not configured yet.[/yellow]")


if __name__ == "__main__":
    main()