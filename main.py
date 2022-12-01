"""
Advent of Code 2022
"""

import click


@click.command()
@click.option("--day", default=1, help="Day to run")
def run(day):
    """
    Advent of Code 2022

    To Do: Package this up as a CLI app
    """
    click.echo(f"I'm running {day}")


if __name__ == "__main__":
    run()  # pylint: disable=no-value-for-parameter
