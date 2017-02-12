"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a
name score.

For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""


def main():
    print(solve(open('resources/names.txt', 'r').readline()))


def solve(names_text):
    names = sorted(names_text.replace('"', "").split(","))
    scores = [sum(map(char_score, list(name))) * (names.index(name) + 1)
              for name in names]
    return sum(scores)


def char_score(char):
    return ord(char.lower()) - 96


if __name__ == "__main__":
    main()