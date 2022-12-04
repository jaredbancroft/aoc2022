"""
Day 4
"""


def solution() -> None:
    """
    Camp Cleanup
    """
    with open("puzzle_inputs/day4.txt", "r", encoding="utf-8") as file:
        lines = file.read().splitlines()

    total_part1 = 0
    total_part2 = 0

    for line in lines:
        elf1, elf2 = line.split(",")
        start1, end1 = elf1.split("-")
        start2, end2 = elf2.split("-")
        assignment1 = set(range(int(start1), int(end1) + 1))
        assignment2 = set(range(int(start2), int(end2) + 1))

        if assignment1.issubset(assignment2) or assignment2.issubset(
            assignment1
        ):
            total_part1 += 1

        if assignment1.intersection(assignment2):
            total_part2 += 1

    print(total_part1)
    print(total_part2)


if __name__ == "__main__":
    solution()
