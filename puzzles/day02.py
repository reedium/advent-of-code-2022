"""
Advent of Code 2022 - Day 02

Run with:
    python puzzles/day02.py inputs/day02.txt
"""
import pathlib
import sys
from typing import Dict, List, Tuple


class Game:
    scores = {"win": 6, "draw": 3, "loss": 0, "moves": {"Rock": 1, "Paper": 2, "Scissors": 3}}
    rules = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}

    def __init__(self, moves) -> None:
        self.moves = moves

    def strategy1(self) -> int:
        mapping = {"A": "Rock", "B": "Paper", "C": "Scissors", "X": "Rock", "Y": "Paper", "Z": "Scissors"}

        score = 0
        for move in self.moves:
            player = mapping[move[1]]
            opponent = mapping[move[0]]
            if self.rules[player] == opponent:
                score += self.scores["win"]
            elif player == opponent:
                score += self.scores["draw"]
            else:
                score += self.scores["loss"]

            score += self.scores["moves"][player]
        return score

    def strategy2(self) -> int:
        mapping = {"A": "Rock", "B": "Paper", "C": "Scissors", "X": "loss", "Y": "draw", "Z": "win"}

        score = 0
        for move in self.moves:
            opponent = mapping[move[0]]
            expected_result = mapping[move[1]]
            if expected_result == "win":
                player = [k for k, v in self.rules.items() if v == opponent][0]
            elif expected_result == "draw":
                player = opponent
            else:
                player = self.rules[opponent]

            score += self.scores[expected_result]
            score += self.scores["moves"][player]
        return score


def part1(inputs: List[List[str]]) -> int:
    game = Game(inputs)
    return game.strategy1()


def part2(inputs: List[List[str]]) -> int:
    game = Game(inputs)
    return game.strategy2()


def parse(inputs: str) -> List[List[str]]:
    return [[value for value in line.split()] for line in inputs.split("\n")]


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
