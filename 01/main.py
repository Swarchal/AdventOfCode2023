import re
import string
import sys


def read_input(path: str) -> list[str]:
    with open(path, "r") as f:
        return [i.strip() for i in f.readlines()]


def get_digits(line: str) -> int:
    digits = [i for i in line if i.isdigit()]
    return int(digits[0] + digits[-1])


# part 2
digit_str = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digit_map = {k: v for k, v in zip(digit_str, string.digits[1:])}


def get_digits2(line: str) -> int:
    possible = digit_str + list(string.digits)
    found = re.findall(rf"(?=({'|'.join(possible)}))", line)
    return int(digit_map.get(found[0], found[0]) + digit_map.get(found[-1], found[-1]))


def main():
    data = read_input(sys.argv[1])
    print(sum(get_digits(i) for i in data))
    print(sum(get_digits2(i) for i in data))


if __name__ == "__main__":
    main()
