"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?"""
from itertools import islice


def main():
    print(solve(10001))


def solve(number):
    primes = gen_primes()
    return list(islice(primes, number - 1, number))[0]


def gen_primes():
    p = 2
    yield p
    primes = [p]
    while True:
        p += 1
        if 0 not in [p % x for x in primes]:
            primes.append(p)
            yield p


if __name__ == "__main__":
    main()