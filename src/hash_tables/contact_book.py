import contextlib

from src.hash_tables.direct_address import DirectAddressMap
from src.hash_tables.open_address import OpenAddressHashMap

MAX_NUMBER = 10_000_000
PRIME = 11


def h(key: int) -> int:
    return key * PRIME


def contact_book_direct_address(queries: list[tuple[str, str, str]]) -> list[str]:
    d = DirectAddressMap[str](MAX_NUMBER)
    result: list[str] = []
    for query in queries:
        command = query[0]
        if command == "add":
            d.add(int(query[1]), query[2])
        elif command == "find":
            result.append(d.get(int(query[1]), "not found"))
        elif command == "del":
            with contextlib.suppress(KeyError):
                d.delete(int(query[1]))
        else:
            raise NotImplementedError
    return result


def contact_book_open_address(queries: list[tuple[str, str, str]]) -> list[str]:
    d = OpenAddressHashMap[int, str](h, len(queries))
    result: list[str] = []
    for query in queries:
        command = query[0]
        if command == "add":
            d.add(int(query[1]), query[2])
        elif command == "find":
            result.append(d.get(int(query[1]), "not found"))
        elif command == "del":
            with contextlib.suppress(KeyError):
                d.delete(int(query[1]))
        else:
            raise NotImplementedError
    return result
