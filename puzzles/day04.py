"""
Advent of Code 2022 - Day 04

Run with:
    python puzzles/day04.py inputs/day04.txt
"""
import pathlib
import sys
from typing import Dict, List, Tuple


class Game:
    inputs = []
    def __init__(self, inputs) -> None:
        self.inputs = inputs

    def solve(self, coverage):
        covered_count = 0
        for line in self.inputs:
            elf1, elf2 = line.split(",")
            e1_start, e1_end = elf1.split("-")
            e2_start, e2_end = elf2.split("-")
            if coverage == "complete":
                covered_count += self.is_fully_covered(int(e1_start), int(e1_end), int(e2_start), int(e2_end))
            elif coverage == "partial":
                covered_count += self.is_partially_covered(int(e1_start), int(e1_end), int(e2_start), int(e2_end))

        return covered_count

    @staticmethod
    def is_fully_covered(e1_start, e1_end, e2_start, e2_end) -> bool:
        e1_range = range(e1_start, e1_end + 1)
        e2_range = range(e2_start, e2_end + 1)
        if e1_start == e1_end and int(e1_start) in e2_range:
            return True
        elif e2_start == e2_end and int(e2_start) in e1_range:
            return True
        elif e1_range.start in e2_range and e1_range[-1] in e2_range:
            return True
        elif e2_range.start in e1_range and e2_range[-1] in e1_range:
            return True

        return False

    @staticmethod
    def is_partially_covered(e1_start, e1_end, e2_start, e2_end) -> bool:
        e1_range = range(e1_start, e1_end + 1)
        e2_range = range(e2_start, e2_end + 1)
        if int(e1_start) in e2_range or int(e1_end) in e2_range:
            return True
        elif int(e2_start) in e1_range or int(e2_end) in e1_range:
            return True
        return False



def part1(inputs: List[List[str]]) -> int:
    game = Game(inputs)
    return game.solve("complete")


def part2(inputs: List[List[str]]) -> int:
    game = Game(inputs)
    return game.solve("partial")


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
