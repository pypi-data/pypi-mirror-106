from pyfactcast.client.entities import Fact
from typing import Iterable
from pyfactcast.client.sync import FactStore


fact_store = FactStore()


def subscribe(namespace: str, follow: bool) -> Iterable[Fact]:
    with fact_store as fs:
        return fs.subscribe(namespace=namespace, continuous=follow)
