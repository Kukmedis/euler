"""
Euler discovered the remarkable quadratic formula:
n^2 + n + 41
It turns out that the formula will produce 40 primes for the consecutive
integer values 0 ≤ n ≤ 39.
However, when n = 40, 40^2 + 40 + 41 =40(40 + 1) + 41 is divisible by 41,
and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula n^2 − 79n + 1601 was discovered, which produces
80 primes for the consecutive values 0 ≤ n ≤ 79.
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n^2 + an + b, where |a| < 1000 and |b| ≤ 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n = 0.
"""
from itertools import takewhile, count


def main():
    print(solve())


def solve():
    primes = list(gen_primes(10000))
    prime_scores = {(a, b): num_of_cons_primes(a, b, primes)
                    for a in range(-999, 1000)
                    for b in range(-1000, 1001)}
    max_pair = max(prime_scores, key=prime_scores.get)
    return max_pair[0] * max_pair[1]


def num_of_cons_primes(a, b, primes):
    return sum(1 for i in
               takewhile(lambda x: x in primes,
                        (n ** 2 + (a * n) + b for n in count())))


def gen_primes(up_to):
    p = 2
    yield p
    primes = [p]
    while p < up_to:
        p += 1
        if 0 not in [p % x for x in primes]:
            primes.append(p)
            yield p


if __name__ == "__main__":
    main()