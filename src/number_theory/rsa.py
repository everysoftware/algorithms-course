from math import gcd


# O(n + log e), e - открытый ключ
def encrypt(p: int, q: int, e_start: int, plaintext: str) -> list[int]:
    public_key, _ = generate_keypair(p, q, e_start)
    encrypted = encrypt_with_public(plaintext, public_key)
    return encrypted


# O(p*q)
def generate_keypair(p: int, q: int, e_start: int) -> tuple[tuple[int, int], tuple[int, int]]:
    n = p * q
    phi = (p - 1) * (q - 1)
    # Создание открытого ключа
    e = e_start
    g = gcd(e, phi)
    while g != 1:
        e += 1
        g = gcd(e, phi)
    # Создание закрытого ключа
    d = pow(e, -1, phi)
    return (e, n), (d, n)


# O(n + log e), e - открытый ключ
def encrypt_with_public(plaintext: str, public_key: tuple[int, int]) -> list[int]:
    e, n = public_key
    data_bytes = plaintext.encode("utf-8")
    encrypted = pow(int.from_bytes(data_bytes), e, n)
    # Переводим число в список байтов -
    bytes_list = to_bytes(encrypted)
    return bytes_list


# O(log n)
def to_bytes(n: int) -> list[int]:
    bytes_list = []
    while n != 0:
        bytes_list.append(n & 0xFF)  # n % 256
        n >>= 8  # n //= 256
    return bytes_list[::-1]
