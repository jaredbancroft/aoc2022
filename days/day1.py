"""
Day 1
"""


def solution():
    """
    Elven Calorie Counter
    """

    with open(
        "puzzle_inputs/day1.txt", "r", encoding="utf-8"
    ) as f:  # pylint: disable=invalid-name
        lines = f.read().splitlines()

    current_calories = 0
    calories = []

    for line in lines:
        if line == "":
            calories.append(current_calories)
            current_calories = 0
        else:
            current_calories += int(line)

    calories.sort(reverse=True)

    print(f"Max calories carried {calories[0]}")
    print(f"Top 3 calorie total: {calories[0] + calories[1] + calories[2]}")


if __name__ == "__main__":
    solution()
