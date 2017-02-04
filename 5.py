"""2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all
of the numbers from 1 to 20?"""
from functools import reduce


def main():
    print(solve(20))


def solve(number):
    all_factors = [generate_factors(n) for n in range (2, number + 1)]
    merged_factors = reduce(merge_factors, all_factors)
    return reduce(lambda x, y: x * y, merged_factors)


def merge_factors(factors_1, factors_2):
    factors_1 = list(factors_1)
    factors_2 = list(factors_2)
    factor_set = set(factors_1 + factors_2)
    merged_factors = [[x] * max(factors_1.count(x), factors_2.count(x))
                      for x in factor_set]
    return [y for x in merged_factors for y in x]


def generate_factors(number):
    prime_generator = gen_primes()
    prime = next(prime_generator)
    while prime <= number:
        if number % prime == 0:
            number //= prime
            yield prime
        else:
            prime = next(prime_generator)


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