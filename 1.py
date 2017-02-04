"""If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000."""


def main():
    print(solve(1000))


def solve(number):
    numbers = range(1, number)
    multiples_of_3_and_5 = filter(lambda x: x % 3 == 0 or x % 5 == 0, numbers)
    answer = sum(multiples_of_3_and_5)
    return answer


if __name__ == "__main__":
    main()