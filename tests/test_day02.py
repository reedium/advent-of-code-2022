import pathlib
import pytest
import sys

ROOT_DIR = pathlib.Path(__file__).parent.parent
sys.path.append(f"{ROOT_DIR}/puzzles")
import day02 as aoc

INPUTS_DIR = f"{ROOT_DIR}/inputs"

@pytest.fixture
def example_data():
    input_path = f"{INPUTS_DIR}/day02-example.txt"
    return aoc.parse(pathlib.Path(input_path).read_text().strip())


@pytest.fixture
def day02_data():
    input_path = f"{INPUTS_DIR}/day02.txt"
    return aoc.parse(pathlib.Path(input_path).read_text().strip())


def test_example1(example_data):
    assert aoc.part1(example_data) == 15


def test_example2(example_data):
    assert aoc.part2(example_data) == 12


def test_part1(day02_data):
    assert aoc.part1(day02_data) == 12679


def test_part2(day02_data):
    assert aoc.part2(day02_data) == 14470
