def extract_color_counts(hand):
    colors_counts = {"red": 0, "green": 0, "blue": 0}
    colors = hand.rstrip().split(",")
    for color in colors:
        _, count, color = color.split(" ")
        colors_counts[color] = int(count)
    return colors_counts


def part1():
    AVAILABLE_RED = 12
    AVAILABLE_GREEN = 13
    AVAILABLE_BLUE = 14
    game_id_sum = 0
    with open("input.txt") as file:
        for line in file:
            # Extract game ID
            game_id, hands = line.split(":")
            game_id = int(game_id.split(" ")[-1])
            # Extract each hand
            hands = hands.split(";")
            # Extract color counts
            for hand in hands:
                color_counts = extract_color_counts(hand)
                if (
                    AVAILABLE_RED - color_counts["red"] < 0
                    or AVAILABLE_GREEN - color_counts["green"] < 0
                    or AVAILABLE_BLUE - color_counts["blue"] < 0
                ):
                    break
            else:
                game_id_sum += game_id

    print(game_id_sum)


def part2():
    AVAILABLE_RED = 12
    AVAILABLE_GREEN = 13
    AVAILABLE_BLUE = 14
    power_sum = 0
    with open("input.txt") as file:
        for line in file:
            # Extract each hand
            _, hands = line.split(":")
            hands = hands.split(";")
            # Extract color counts and add if larger than stored counts
            needed_colors_counts = {"red": 0, "green": 0, "blue": 0}
            for hand in hands:
                hand_color_counts = extract_color_counts(hand)
                for color in ["red", "green", "blue"]:
                    needed_colors_counts[color] = max(hand_color_counts[color], needed_colors_counts[color])

            # Calculate power of set
            power = 1 # Can't be zero since we are multiplying
            for _, count in needed_colors_counts.items():
                power *= count
            power_sum += power

    print(power_sum)


if __name__ == "__main__":
    # part1()
    part2()
