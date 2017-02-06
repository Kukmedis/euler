"""The following iterative sequence is defined for
the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million."""


def main():
    print(solve(1000000))


def solve(number):
    return max(range(1, number),
               key=lambda i: len(list(generate_sequence(i))))


def generate_sequence(start):
    next_number = start
    yield next_number
    while next_number != 1:
        if next_number % 2 == 0:
            next_number //= 2
        else:
            next_number = 3 * next_number + 1
        yield next_number


if __name__ == "__main__":
    main()