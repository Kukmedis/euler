"""
In England the currency is made up of pound, £, and pence, p,
and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?"""


def main():
    print(solve())


def solve():
    # a - 10 b - 20 c - 50 d - 100 e - 200
    five = {"11111", "1112", "122", "5"}
    ten = unique_products(five, five) | {"a", "22222"}
    twenty = unique_products(ten, ten) | {"b"}
    fifty = unique_products(ten, unique_products(twenty, twenty)) | {"c"}
    hundred = unique_products(fifty, fifty) | {"d", "bbbbb"}
    two_hundreds = unique_products(hundred, hundred) | {"e"}
    return len(two_hundreds)


def unique_products(coins1, coins2):
    return {"".join(sorted(x + y)) for x in coins1 for y in coins2}


if __name__ == "__main__":
    main()