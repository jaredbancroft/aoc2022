"""
Day 5
"""

from collections import defaultdict, deque
from copy import deepcopy
from typing import Any, DefaultDict
from dataclasses import dataclass


@dataclass
class Instruction:
    """
    Tell the crane what to do
    """

    number_of_crates: int
    from_stack_number: int
    to_stack_number: int


class Crane:
    """
    Here to move crates according to a stack state and set of instructions
    """

    def __init__(
        self,
        stack_state: DefaultDict[Any, list],
        instruction_set: list[Instruction],
        use_9001: bool = False,
    ) -> None:
        self.stack_state = stack_state
        self.instruction_set = instruction_set
        self.use_9001 = use_9001

    def print(self) -> None:
        """
        Print out the stack state
        """
        print(self.stack_state)

    def run_instruction_set(self) -> None:
        """
        Run the set of instructions
        """
        for instruction in self.instruction_set:
            self._run_instruction(instruction)

        print(self._get_top_crates())

    def _run_instruction(self, instruction: Instruction) -> None:
        if self.use_9001:
            self._move2(
                instruction.number_of_crates,
                instruction.from_stack_number,
                instruction.to_stack_number,
            )
        else:
            for _ in range(0, instruction.number_of_crates):
                self._move(
                    instruction.from_stack_number, instruction.to_stack_number
                )

    def _move(self, from_stack_number: int, to_stack_number: int) -> None:
        crate = self.stack_state[from_stack_number].pop()
        self.stack_state[to_stack_number].append(crate)

    def _move2(
        self,
        number_of_crates: int,
        from_stack_number: int,
        to_stack_number: int,
    ) -> None:
        crates = deque()

        for _ in range(number_of_crates):
            crates.appendleft(self.stack_state[from_stack_number].pop())

        for _ in range(number_of_crates):
            self.stack_state[to_stack_number].append(crates.popleft())

    def _get_top_crates(self) -> str:
        top_crates: list[str] = []
        for i in range(0, len(self.stack_state)):
            top_crate = self.stack_state[i + 1].pop()
            top_crates.append(top_crate)

        return "".join(top_crates)


def parse_stack_state(crates: list) -> DefaultDict[Any, list]:
    """
    Parse stupid input
    """
    stacks = defaultdict(list)

    for crate in reversed(crates):
        stack_number = 1
        for i in range(0, len(crate), 4):
            if crate[i + 1] != " ":
                stacks[stack_number].append(crate[i + 1])
            stack_number += 1

    return stacks


def parse_instructions(text_instructions: list[str]) -> None:
    """
    Parses the puzzle instructions into an InstructionSet
    """
    instruction_set: list[Instruction] = []

    for text_instruction in text_instructions:
        (
            _,
            number_of_crates,
            _,
            from_stack_number,
            _,
            to_stack_number,
        ) = text_instruction.split()
        instruction = Instruction(
            int(number_of_crates), int(from_stack_number), int(to_stack_number)
        )
        instruction_set.append(instruction)

    return instruction_set


def solution() -> None:
    """
    Solve the puzzle
    """
    with open("puzzle_inputs/day5.txt", "r", encoding="utf-8") as file:
        lines = file.read().splitlines()

    idx = lines.index("")
    initial_puzzle_state = lines[: idx - 1]
    puzzle_instructions = lines[idx + 1 :]

    stack_state = parse_stack_state(initial_puzzle_state)
    instruction_set = parse_instructions(puzzle_instructions)

    crane_part1 = Crane(deepcopy(stack_state), instruction_set)
    crane_part1.run_instruction_set()

    crane_part2 = Crane(stack_state, instruction_set, use_9001=True)
    crane_part2.run_instruction_set()


if __name__ == "__main__":
    solution()
