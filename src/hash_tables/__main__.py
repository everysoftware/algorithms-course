import sys


from contact_book import contact_book, h
from chain_hashing_map import chain_hashing
from pattern_search import pattern_search2
from open_address_map import OpenAddressMap


def test_contact_book():
    n = int(input())
    queries = [input().split() for _ in range(n)]
    print(*contact_book(n, queries), sep="\n")


def test_map_memory_usage():
    home_d = {
        20: "roma",
        23: "ann",
        33: "oleg",
        58: "diana",
        90: "alex",
        21: "nikita",
        111: "vlad",
        120: "elena",
        2: "me",
    }
    my_d = OpenAddressMap(h)
    for key in home_d:
        my_d.add(key, home_d[key])
    print(f"Home dictionary: {sys.getsizeof(home_d)}")
    print(f"My dictionary: {sys.getsizeof(my_d)}")


def test_chain_hashing():
    m = int(input())
    n = int(input())
    queries = [input().split() for _ in range(n)]
    print(*chain_hashing(m, n, queries), sep="\n")


def test_pattern_search():
    pattern = input()
    text = input()
    print(*pattern_search2(pattern, text))


def main():
    f = [
        ("Task #1. Contact book", test_contact_book),
        ("Map memory usage", test_map_memory_usage),
        ("Task #2. Chain hashing", test_chain_hashing),
        ("Task #3. Pattern search", test_pattern_search),
    ]
    for i, x in enumerate(f):
        print(f"{i + 1}. {x[0]}")
    n = int(input())
    if n > len(f):
        print("Unknown command")
    else:
        f[n - 1][1]()


main()
