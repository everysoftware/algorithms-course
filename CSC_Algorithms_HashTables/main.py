from contact_book import *


def test_contact_book():
    n = int(input())
    queries = [input().split() for _ in range(n)]
    print(*contact_book(n, queries), sep='\n')


def main():
    f = [
        ('Task #1. Contact book', test_contact_book)
    ]
    for i, x in enumerate(f):
        print(f'{i + 1}. {x[0]}')
    n = int(input())
    if n > len(f):
        print('Unknown command')
    else:
        f[n - 1][1]()


main()
