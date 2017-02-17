"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
from functools import reduce


def main():
    print(solve(10000000))


def solve(number):
    factorials = {str(x): reduce(lambda a, b: a * b, range(1, x + 1))
                  for x in range(1, 10)}
    factorials['0'] = 1
    curious_nums = [n for n in range(3, number)
                    if sum(map(lambda x: factorials[x], list(str(n)))) == n]
    return sum(curious_nums)


if __name__ == "__main__":
    main()