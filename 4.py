"""A palindromic number reads the same both ways. The largest palindrome made
 from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""
from itertools import combinations_with_replacement


def main():
    print(solve())


def solve():
    for p in palindromes():
        for n in range(999, 99, -1):
            if p % n == 0 and len(str(p // n)) == 3:
                return p


def palindromes():
    digits = range(9, -1, -1)
    half = [(x, y, z) for x in digits for y in digits for z in digits]
    return map(lambda x: int(''.join(map(str, x + x[::-1]))), half)


if __name__ == "__main__":
    main()