import typer
from rich.console import Console

import pyfactcast.app.business.enumerate as business

app = typer.Typer()
console = Console()


@app.command()
def namespaces() -> None:
    for namespace in sorted(business.namespaces()):
        console.print(namespace, style="bold green")


@app.command()
def types(namespace: str) -> None:
    for type in sorted(business.types(namespace)):
        console.print(type, style="bold green")
