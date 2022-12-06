"""
Day 6
"""


START_OF_PACKET = 4
START_OF_MESSAGE = 14


def detect_distinct(line: str, mode: str = "packet") -> int:
    """
    Do all the stuff
    """
    subroutine: set = set()

    if mode == "packet":
        terminator = START_OF_PACKET
    elif mode == "message":
        terminator = START_OF_MESSAGE
    else:
        return -2

    for i in range(0, len(line)):
        for j in range(i, len(line)):
            if line[j] not in subroutine:
                subroutine.add(line[j])
                if len(subroutine) == terminator:
                    return j + 1
            else:
                subroutine.clear()
                break

    return -1


def solution() -> None:
    """
    Tuning Trouble
    """
    with open("puzzle_inputs/day6.txt", "r", encoding="utf-8") as file:
        line: str = file.readline()

    part1 = detect_distinct(line, "packet")
    part2 = detect_distinct(line, "message")
    print(part1)
    print(part2)


if __name__ == "__main__":
    solution()
