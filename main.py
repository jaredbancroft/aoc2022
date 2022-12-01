"""
Advent of Code 2022
"""

import argparse


def run(day):
    """
    Runner
    """
    print(f"I'm running {day}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code 2022")
    parser.add_argument("day")
    args = parser.parse_args()
    run(args.day)
