"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician
in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less
than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
"""
from fractions import Fraction
from functools import reduce
from itertools import starmap


def main():
    print(solve())


def solve():
    all_fractions = [(x, y) for x in range(11, 50) for y in range(50, 100)]
    pairs = filter(lambda pair: is_curious(pair[0], pair[1]), all_fractions)
    return reduce(lambda x, y: x * y, starmap(Fraction, pairs)).denominator


def curious_simplify(x, y):
    x_set, y_set = set(str(x)), set(str(y))
    if len(x_set) == len(y_set) == 2 \
            and "0" not in x_set and "0" not in y_set and x_set != y_set\
            and len(x_set ^ y_set) == 2:
        return int("".join(x_set - y_set)), int("".join(y_set - x_set))
    else:
        return x, y


def is_curious(x, y):
    cs_x, cs_y = curious_simplify(x, y)
    return (cs_x, cs_y) != (x, y) and cs_x / cs_y == x / y


if __name__ == "__main__":
    main()