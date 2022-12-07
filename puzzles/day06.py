"""
Advent of Code 2022 - Day 06

Run with:
    python puzzles/day06.py inputs/day06.txt
"""
import pathlib
import sys
from typing import Dict, List, Tuple


class Game:
    inputs = []
    def __init__(self, inputs) -> None:
        self.inputs = inputs

    def find_packet_uniqueness(self, uniqueness):
        cache = self.inputs[:uniqueness]
        # Index starts at 0, add uniqueness for actual character location
        for index, char in enumerate(self.inputs[uniqueness:]):
            cache = cache[1:] + char # FIFO
            if len(set(cache)) == uniqueness:
                return index + 1 + uniqueness


def part1(inputs: List[List[str]]) -> int:
    game = Game(inputs)
    return game.find_packet_uniqueness(4)


def part2(inputs: List[List[str]]) -> int:
    game = Game(inputs)
    return game.find_packet_uniqueness(14)


def parse(inputs: str) -> List[List[str]]:
    return inputs



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
