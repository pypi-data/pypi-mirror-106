from uuid import UUID
import typer
from rich.console import Console
from rich.table import Table
from datetime import datetime
import json

import pyfactcast.app.business.streams as business

app = typer.Typer()
console = Console()


@app.command()
def subscribe(
    namespace: str,
    follow: bool = typer.Option(
        False, "--follow", help="Stay connected and listen for new events."
    ),
    from_now: bool = typer.Option(
        False, "--from-now", help="Follow the event stream starting now."
    ),
    after_fact: UUID = typer.Option(
        None, help="Get all events in the stream that happened after a certain ID."
    ),
    json_format: bool = typer.Option(False, "--json", help="Output raw json events."),
) -> None:
    subscription = business.subscribe(
        namespace=namespace, follow=follow, after_fact=after_fact, from_now=from_now
    )
    """
    Subscribe to an eventstream.
    """

    if json_format:
        for elem in subscription:
            console.print(elem.json(indent=2))

    for elem in subscription:
        table = Table(show_header=False, show_lines=True, header_style="bold magenta")
        table.add_column("Time")
        table.add_column("Type")
        table.add_column("Header")
        table.add_column("Payload")
        table.add_row(
            datetime.fromtimestamp(int(elem.header.meta["_ts"][:10])).isoformat(),  # type: ignore
            elem.header.type,
            elem.header.json(indent=2),
            json.dumps(elem.payload, indent=2),
        )
        console.print(table)
