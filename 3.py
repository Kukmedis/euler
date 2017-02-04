"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?"""


def main():
    print(solve(600851475143))


def solve(number):
    return max(generate_factors(number))


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