"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""


def main():
    print(solve(1000))


def solve(number):
    return sum(map(int, list(str(2 ** number))))


if __name__ == "__main__":
    main()