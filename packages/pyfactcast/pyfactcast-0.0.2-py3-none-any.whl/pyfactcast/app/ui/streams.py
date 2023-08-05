import typer
from rich.console import Console

import pyfactcast.app.business.streams as business

app = typer.Typer()
console = Console()


@app.command()
def subscribe(namespace: str, follow: bool = False) -> None:
    for elem in business.subscribe(namespace, follow):
        console.print(elem)
