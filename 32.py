"""
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number,
15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254,
containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure
to only include it once in your sum.
"""
from itertools import permutations


def main():
    print(solve())


def solve():
    all_combinations = list(map(list, permutations(range(1, 10))))
    one_fours = {numbers[0] * join_ints(numbers[1:5])
                 for numbers in all_combinations
                 if numbers[0] * join_ints(numbers[1:5])
                 == join_ints(numbers[5:9])}
    two_threes = {join_ints(numbers[0:2]) * join_ints(numbers[2:5])
                  for numbers in all_combinations
                  if join_ints(numbers[0:2]) * join_ints(numbers[2:5])
                  == join_ints(numbers[5:9])}
    return sum(one_fours | two_threes)


def join_ints(ints):
    return int("".join(map(str, ints)))


if __name__ == "__main__":
    main()