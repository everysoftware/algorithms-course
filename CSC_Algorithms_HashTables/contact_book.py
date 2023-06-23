from open_address_map import OpenAddressMap


PRIME = 11


def h(key, m):
    return (int(key) * PRIME) % m


def contact_book(n, queries):
    # без указания размера был TL =(
    d = OpenAddressMap(h, n)
    result = []
    for query in queries:
        command = query[0]
        if command == 'add':
            d.add(query[1], query[2])
        elif command == 'find':
            result.append(d.get(query[1], 'not found'))
        elif command == 'del':
            try:
                d.delete(query[1])
            except KeyError:
                pass
        else:
            raise NotImplementedError
    return result
