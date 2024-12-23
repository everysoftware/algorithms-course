from src.number_theory import generate_keypair, encrypt
from src.number_theory import primality_tests


def encrypt_view() -> None:
    p, q, e_start = list(map(int, input().split()))
    plaintext = input().strip()
    public, private = generate_keypair(p, q, e_start)
    encrypted = encrypt(plaintext, public)

    print("Private:", *private)
    print("Public:", *public)
    print("Initial bytes:", *[b for b in plaintext.encode("utf-8")])
    print("Encrypted bytes:", *encrypted)


def primality_tests_view() -> None:
    n = int(input())
    mb_successful, fermat_successful = primality_tests(n)
    mb_composite_candidates = (n - 1) - sum(mb_successful)
    fermat_composite_candidates = (n - 1) - fermat_successful

    print(
        "Miller-Rabin test:",
        mb_composite_candidates == 0,
        mb_composite_candidates,
        mb_successful[0],
        mb_successful[1],
    )
    print(
        "Fermat test:",
        fermat_composite_candidates == 0,
        fermat_composite_candidates,
        fermat_successful,
    )
