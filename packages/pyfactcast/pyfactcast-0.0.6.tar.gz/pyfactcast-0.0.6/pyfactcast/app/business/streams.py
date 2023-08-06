import re
from uuid import UUID
from pyfactcast.client.entities import Fact
from typing import Iterable, List
from pyfactcast.client.sync import FactStore


fact_store = FactStore()


def filter_types(*, fs: FactStore, namespace: str, it: Iterable[str]) -> Iterable[str]:
    if not it:
        return it

    types_for_namespace = fs.enumerate_types(namespace=namespace)
    res = set()

    # TODO: Make the regex stuff beautiful
    regexes = [re.compile(elem) for elem in it]
    for regexp in regexes:
        res.update(list(filter(regexp.fullmatch, types_for_namespace)))

    return res


def subscribe(
    namespace: str,
    follow: bool,
    from_now: bool = False,
    after_fact: UUID = None,
    fact_types: List[str] = [],
) -> Iterable[Fact]:

    with fact_store as fs:
        return fs.subscribe(
            namespace=namespace,
            continuous=follow,
            from_now=from_now,
            after_fact=after_fact,
            fact_types=filter_types(fs=fs, namespace=namespace, it=fact_types),
        )
