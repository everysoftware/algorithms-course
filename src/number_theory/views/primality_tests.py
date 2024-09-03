from src.number_theory import primality_tests


def primality_tests_view():
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
