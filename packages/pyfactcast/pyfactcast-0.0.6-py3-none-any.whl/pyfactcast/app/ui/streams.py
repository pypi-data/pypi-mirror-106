from typing import Iterable, List
from uuid import UUID
import typer
from rich.console import Console
from rich.table import Table
from datetime import datetime
import json

import pyfactcast.app.business.streams as business

app = typer.Typer()
console = Console()


def print_iterable_as_json_list(
    iterable: Iterable,
) -> None:
    console.print("[")
    it = iter(iterable)

    try:
        last = next(it)  # type: ignore
    except StopIteration:
        console.print("]")
        return

    for elem in it:
        console.print(f"{last.json(indent=2)},", soft_wrap=True)
        last = elem
    console.print(last.json(indent=2), soft_wrap=True)
    console.print("]")


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
    fact_types: List[str] = typer.Option(
        [],
        "--type",
        help="The types of events to get. Can be used multiple times. Supports regexp.",
    ),
) -> None:
    subscription = business.subscribe(
        namespace=namespace,
        follow=follow,
        after_fact=after_fact,
        from_now=from_now,
        fact_types=fact_types,
    )
    """
    Subscribe to an eventstream.
    """

    if json_format:
        print_iterable_as_json_list(subscription)
        return

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
