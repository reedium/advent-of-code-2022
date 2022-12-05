"""
Advent of Code 2022 - Day 01

Run with:
    python puzzles/day01.py inputs/day01.txt
"""
import pathlib
import sys
from typing import List, Tuple

def part1(inputs: List[int]) -> int:
    largest = max(inputs, key=sum)
    return sum(largest)


def part2(inputs: List[int]) -> int:
    sums = sorted([sum(x) for x in inputs])
    return sum(sums[-3:])


def parse(inputs: str) -> List[List[int]]:
    return [[int(value) for value in line.split()] for line in inputs.split("\n\n")]


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
