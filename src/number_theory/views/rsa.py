from src.number_theory import generate_keypair, encrypt


def encrypt_view():
    p, q, e_start = list(map(int, input().split()))
    plaintext = input().strip()
    public, private = generate_keypair(p, q, e_start)
    encrypted = encrypt(plaintext, public)

    print("Private:", *private)
    print("Public:", *public)
    print("Initial bytes:", *[b for b in plaintext.encode("utf-8")])
    print("Encrypted bytes:", *encrypted)
