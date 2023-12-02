NUM_STR_TO_INT = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def check_for_spelling_at_character(i, str, reversed=False):
    available_chars = len(str) - i
    if available_chars < 3:
        return None
    for length in range(3, min(available_chars, 5) + 1):
        sub_str = str[i : i + length]
        if reversed:
            sub_str = sub_str[::-1]
        if sub_str in NUM_STR_TO_INT:
            return NUM_STR_TO_INT[sub_str]


def part2():
    sum = 0
    with open("data.txt") as file:
        for line in file:
            first_digit = None
            second_digit = None
            for i, c in enumerate(line):
                if c.isdigit():
                    first_digit = c
                    break
                first_digit = check_for_spelling_at_character(i, line)
                if first_digit:
                    break

            rev_line = line[::-1]
            for i, c in enumerate(rev_line):
                if c.isdigit():
                    second_digit = c
                    break
                second_digit = check_for_spelling_at_character(
                    i, rev_line, reversed=True
                )
                if second_digit:
                    break

            sum += int(f"{first_digit}{second_digit}")

    print(sum)


def part1():
    sum = 0
    with open("data.txt") as file:
        for line in file:
            first_digit = None
            second_digit = None
            for c in line:
                if c.isdigit():
                    first_digit = c
                    break
            for c in line[::-1]:
                if c.isdigit():
                    second_digit = c
                    break

            sum += int(f"{first_digit}{second_digit}")

    print(sum)


if __name__ == "__main__":
    part1()
    part2()
