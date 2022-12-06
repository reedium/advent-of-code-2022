"""
Advent of Code 2022 - Day 03

Run with:
    python puzzles/day03.py inputs/day03.txt
"""
import pathlib
import string
import sys
from typing import Dict, List, Tuple


# Each letter is a type of item (case sensitive)
# Each line is 2 containers (half items in one, half in the other)
# Priorities:
#   * Lowercase: 1-26
#   * Uppercase: 27-52

# Q: Find the item type that appears in both containers. What is the sum of the priories
# Q: Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?


class Game:
    inputs = []
    def __init__(self, inputs) -> None:
        self.inputs = inputs

    def puzzle1(self) -> None:
        score = 0
        for line in self.inputs:
            container1 = list(line[:len(line) // 2])
            container2 = list(line[len(line) // 2:])
            unique_set = set(container1).intersection(container2)
            score += self.score_list(unique_set)

        return score

    def puzzle2(self) -> None:
        score = 0
        for pack in range(0, len(self.inputs), 3):
            unique_set = set(self.inputs[pack]).intersection(self.inputs[pack+1]).intersection(self.inputs[pack+2])
            score += self.score_list(unique_set)

        return score

    @staticmethod
    def score_list(inputs):
        alphabet = string.ascii_lowercase
        score = 0
        for unique in inputs:
            score += alphabet.index(unique.lower())
            score += 1 if unique.islower() else 27
        return score



def part1(inputs: List[List[str]]) -> int:
    game = Game(inputs)
    return game.puzzle1()


def part2(inputs: List[List[str]]) -> int:
    game = Game(inputs)
    return game.puzzle2()


def parse(inputs: str) -> List[List[str]]:
    return [line for line in inputs.split("\n")]


def solve(path: str) -> Tuple[int, int]:
    """Solve the puzzle"""
    puzzle_input = parse(pathlib.Path(path).read_text().strip())
    part1_result = part1(puzzle_input)
    part2_result = part2(puzzle_input)

    return part1_result, part2_result


def main() -> None:
    for path in sys.argv[1:]:
        print(f"Input File: {path}")

        part1_result, part2_result = solve(path)
        print(f"Part 1 Result: {part1_result}")
        print(f"Part 2 Result: {part2_result}")


if __name__ == "__main__":
    main()
