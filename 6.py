"""The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first
one hundred natural numbers and the square of the sum."""


def main():
    print(solve(100))


def solve(number):
    sum_of_numbers = sum(range(1, number + 1))
    sum_squared = sum_of_numbers * sum_of_numbers
    squares_summed = sum(map(lambda x: x * x, range(1, number + 1)))
    return sum_squared - squares_summed


if __name__ == "__main__":
    main()