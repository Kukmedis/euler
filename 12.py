"""The sequence of triangle numbers is generated by adding the natural
numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred
divisors?"""


def main():
    print(solve(500))


def solve(number):
    generator = triangle_generator()
    current_triangle = next(generator)
    while num_of_divisors(current_triangle) <= number:
        current_triangle = next(generator)
    return current_triangle


def triangle_generator():
    last_triangle, num = 0, 0
    while True:
        num += 1
        last_triangle += num
        yield last_triangle


def num_of_divisors(number):
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
    return len(divisors) + 1


if __name__ == "__main__":
    main()