"""
Highly divisible triangular number.

    The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first
ten terms would be: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:
    1: 1
    3: 1,3
    6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

from collections import Counter

def gen_primes():
    D = {}
    q = 2

    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def get_divisors_of(n: int):
    return (x for x in range(1, n+1) if n % x == 0)


def gen_triangular_nums():
    """
    Tn = n(n+1)/2
    """
    n = 1
    tn = 1
    while True:
        yield tn
        n += 1
        tn = n * (n + 1) // 2


def get_len_divisors():
    """
    Get len of divisors of triangular numbers.
    """

    triangulars = gen_triangular_nums()
    primes = gen_primes()
    p = next(primes)
    # tn = next(triangulars)
    tn = 28
    divs = []
    while tn > 1:
        if tn % p == 0:
            tn //= p
            divs.append(p)
        else:
            p = next(primes)
            print(p)
    
    len_ = 1
    for v in list(Counter(divs).items()):
        len_ *= v[1] + 1

    print(len_)


print(get_len_divisors())
