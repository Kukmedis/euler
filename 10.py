"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""


def main():
    print(solve(2000000))


def solve(number):
    return sum(gen_primes(number))


def gen_primes(maximum):
    p = 2
    yield p
    primes = [p]
    while p < maximum:
        p += 1
        if next((False for x in primes if p % x == 0), True):
            primes.append(p)
            yield p


if __name__ == "__main__":
    main()