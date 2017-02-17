"""The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100:
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?"""


def main():
    print(solve(1000000))


def solve(number):
    primes = list(gen_primes(number))
    return len([p for p in primes
                if all(map(lambda x: x in primes, circular_permutations(p)))])


def circular_permutations(number):
    return [int(str(number)[n:] + str(number)[:n])
            for n in range(len(str(number)))]


def gen_primes(max):
    p = 2
    yield p
    primes = [p]
    while p < max:
        p += 1
        if 0 not in (p % x for x in primes):
            primes.append(p)
            yield p


if __name__ == "__main__":
    main()