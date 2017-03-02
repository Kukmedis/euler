"""The number 3797 has an interesting property. Being prime itself,
it is possible to continuously remove digits from left to right,
and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work
from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left
to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes."""
from itertools import islice


def main():
    print(solve())


def solve():
    prime_generator = islice(gen_primes(), 4, None)
    primes = [2, 3, 5, 7]
    trunc_primes = []
    while len(trunc_primes) < 11:
        p = next(prime_generator)
        primes.append(p)
        if is_truncatable(p, primes):
            trunc_primes.append(p)
    return sum(trunc_primes)


def is_truncatable(prime, primes):
    p_str = str(prime)
    return all(is_prime(int(p_str[x:len(p_str)]), primes)
               for x in range(len(p_str))) \
        and all(is_prime(int(p_str[0:x + 1]), primes)
                for x in range(len(p_str) - 1))


def gen_primes():
    p = 2
    yield p
    primes = [p]
    while True:
        p += 1
        if 0 not in (p % x for x in primes):
            primes.append(p)
            yield p


def is_prime(number, primes):
    for prime in primes:
        if number == prime:
            return True
        elif number < prime:
            return False
    return False


if __name__ == "__main__":
    main()