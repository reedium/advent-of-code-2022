"""
Advent of Code 2022 - Day 05

Run with:
    python puzzles/day05.py inputs/day05.txt
"""
import pathlib
import sys
from typing import Dict, List, Tuple
from copy import deepcopy


class Game:
    inputs = []
    def __init__(self, inputs) -> None:
        self.inputs = deepcopy(inputs)

    def move_crates(self, order="LIFO"):
        crates = list(self.inputs["crates"])
        for move in self.inputs["procedures"]:
            number = move[0]
            src_crate = move[1] - 1
            dst_crate = move[2] - 1
            current_stack = []
            for _ in range(number):
                if order == "LIFO":
                    current_stack = [crates[src_crate].pop(0)] + current_stack
                elif order == "FIFO":
                    current_stack.append(crates[src_crate].pop(0))
            crates[dst_crate] = current_stack + crates[dst_crate]
        return ''.join([item[0] for item in crates])

    def part1(self):
        return self.move_crates("LIFO")

    def part2(self):
        return self.move_crates("FIFO")




def parse(inputs: str):
    parsed = {"crates": [], "procedures": []}
    start_diagram, moves = inputs.split("\n\n")

    start_diagram = start_diagram.split("\n")
    parsed["crates"] = [[] for _ in start_diagram.pop().split()]

    for line in start_diagram:
        crate = 0
        for index in range(1, len(line), 4):
            if line[index].strip():
                parsed["crates"][crate].append(line[index])
            crate += 1

    for move in moves.strip().split("\n"):
        words = move.split()
        parsed["procedures"].append([int(words[1]), int(words[3]), int(words[5])])

    return parsed


def part1(inputs: List[List[str]]) -> str:
    game = Game(inputs)
    return game.part1()


def part2(inputs: List[List[str]]) -> str:
    game = Game(inputs)
    return game.part2()



def solve(path: str) -> Tuple[int, int]:
    """Solve the puzzle"""
    puzzle_input = parse(pathlib.Path(path).read_text())
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
