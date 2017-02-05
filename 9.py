"""A Pythagorean triplet is a set of three natural numbers, a < b < c,
for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""
from itertools import product


def main():
    print(solve())


def solve():
    a_b_products = product(range(1, 1000), range(1, 1000))
    a_b = next(a_b for a_b in a_b_products
                if 1000 * a_b[0] + 1000 * a_b[1] - a_b[0] * a_b[1] == 500000)
    a, b, c = a_b[0], a_b[1], 1000 - a_b[0] - a_b[1]
    return a * b * c


if __name__ == "__main__":
    main()