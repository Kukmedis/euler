"""
A unit fraction contains 1 in the numerator. The decimal representation of
the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest
recurring cycle in its decimal fraction part.
"""


def main():
    print(solve(1000))


def solve(number):
    prime_gen = gen_primes(number)
    return max([next((x for x in range(1, number) if 10 ** x % prime == 1), 0)
                for prime in prime_gen]) + 1


def gen_primes(number):
    p = 2
    yield p
    primes = [p]
    while p < number:
        p += 1
        if 0 not in [p % x for x in primes]:
            primes.append(p)
            yield p


if __name__ == "__main__":
    main()