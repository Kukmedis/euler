"""
A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less
than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two abundant
numbers is 24. By mathematical analysis, it can be shown that all integers
greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even
though it is known that the greatest number that cannot be expressed
as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the
sum of two abundant numbers.
"""
from itertools import product


def main():
    print(solve(28124))


def solve(number):
    abundant_numbers = [x for x in range(1, number) if sum_divisors(x) > x]
    abundant_pairs = product(abundant_numbers, abundant_numbers)
    nums = {sum(pair) for pair in abundant_pairs}
    return sum({i for i in range(1, number)} - nums)


def sum_divisors(number):
    return sum(get_divisors(number))


def get_divisors(number):
    initial_number = number
    curr_divisor = 2
    divisors = set()
    while number >= curr_divisor:
        if number % curr_divisor == 0:
            number //= curr_divisor
            additional_divisors = \
                {divisor * curr_divisor for divisor in divisors
                 if divisor * curr_divisor <= initial_number}
            divisors.add(curr_divisor)
            divisors = additional_divisors.union(divisors)
        else:
            curr_divisor += 1
    divisors.discard(initial_number)
    divisors.add(1)
    return divisors


if __name__ == "__main__":
    main()