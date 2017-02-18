"""
The decimal number, 585 = 10010010012 (binary),
is palindromic in both bases.

Find the sum of all numbers, less than one million,
which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base,
may not include leading zeros.)
"""


def main():
    print(solve(1000000))


def solve(number):
    return sum((x for x in range(number)
                if str(x) == str(x)[::-1]
                and "{0:b}".format(x) == "{0:b}".format(x)[::-1]))


if __name__ == "__main__":
    main()