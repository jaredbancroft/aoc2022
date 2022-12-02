"""
Day 2: Rock Paper Scissors
"""


def determine_outcome(opponent, me):  # pylint: disable=invalid-name
    """
    play the game
    """
    if opponent == me:
        return 3

    if (
        (opponent == "rock" and me == "paper")
        or (opponent == "paper" and me == "scissors")
        or (opponent == "scissors" and me == "rock")
    ):
        return 6

    return 0


def determine_shape(opponent, outcome):
    """
    Part 2
    """
    if outcome == 3:
        return opponent

    if determine_outcome(opponent, "rock") == outcome:
        return "rock"

    if determine_outcome(opponent, "paper") == outcome:
        return "paper"

    return "scissors"


def solution():
    """
    Strategy Guide
    """

    with open(
        "puzzle_inputs/day2.txt", "r", encoding="utf-8"
    ) as f:  # pylint: disable=invalid-name
        lines = f.read().splitlines()

    score = 0
    score2 = 0

    guide = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "rock",
        "Y": "paper",
        "Z": "scissors",
    }

    guide2 = {"X": 0, "Y": 3, "Z": 6}

    value = {"rock": 1, "paper": 2, "scissors": 3}

    for line in lines:
        round_inputs = line.split(" ")
        opponent = guide[round_inputs[0]]
        me = guide[round_inputs[1]]  # pylint: disable=invalid-name
        outcome = guide2[round_inputs[1]]

        score += determine_outcome(opponent, me) + value[me]
        score2 += value[determine_shape(opponent, outcome)] + outcome

    print(f"Total score if everything went right? {score}")
    print(f"Total score if we use second methond? {score2}")


if __name__ == "__main__":
    solution()
