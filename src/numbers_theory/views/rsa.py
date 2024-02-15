from numbers_theory import generate_keypair, encrypt


def encrypt_view():
    p, q, e_start = list(map(int, input().split()))
    plaintext = input().strip()
    public, private = generate_keypair(p, q, e_start)
    encrypted = encrypt(plaintext, public)

    print(f"Private:", *private)
    print(f"Public:", *public)
    print(f"Initial bytes:", *[b for b in plaintext.encode("utf-8")])
    print(f"Encrypted bytes:", *encrypted)
