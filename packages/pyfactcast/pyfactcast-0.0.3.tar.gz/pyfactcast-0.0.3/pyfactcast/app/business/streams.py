from uuid import UUID
from pyfactcast.client.entities import Fact
from typing import Iterable
from pyfactcast.client.sync import FactStore


fact_store = FactStore()


def subscribe(
    namespace: str, follow: bool, from_now: bool = False, after_fact: UUID = None
) -> Iterable[Fact]:
    with fact_store as fs:
        return fs.subscribe(
            namespace=namespace,
            continuous=follow,
            from_now=from_now,
            after_fact=after_fact,
        )
