"""
Day 3
"""


def part1(sacks: list[str]) -> int:
    """
    Part 1
    """

    total = 0

    for sack in sacks:
        compartment1 = sack[: len(sack) // 2]
        compartment2 = sack[len(sack) // 2 :]
        match = list(set(compartment1).intersection(set(compartment2)))

        total += (
            ord(match[0]) - 96 if match[0].islower() else ord(match[0]) - 38
        )

    return total


def part2(inputs: list[str]) -> int:
    """
    part 2
    """

    total = 0

    for i in range(0, len(inputs), 3):
        sack1, sack2, sack3 = inputs[i : i + 3]
        match = list(
            set(sack1).intersection(set(sack2)).intersection(set(sack3))
        )

        total += (
            ord(match[0]) - 96 if match[0].islower() else ord(match[0]) - 38
        )

    return total


def solution() -> None:
    """
    do it
    """
    with open("puzzle_inputs/day3.txt", "r", encoding="utf-8") as file:
        inputs = file.read().splitlines()

    print(f"Priority of part1 items: {part1(inputs)}")
    print(f"Priority of part2 items: {part2(inputs)}")


if __name__ == "__main__":
    solution()
