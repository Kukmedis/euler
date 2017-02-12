"""
Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""


def main():
    print(solve(10000))


def solve(number):
    amicable_numbers = {
        i for i in range(1, number)
        if i == sum_divisors(sum_divisors(i)) and i != sum_divisors(i)}
    return sum(amicable_numbers)


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