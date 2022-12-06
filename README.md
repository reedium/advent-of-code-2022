# Overview

My solutions for [Advent of Code](https://adventofcode.com)

Hopefully I keep up with it


# Installation
```
git clone <repo>
cd advent-of-code-2022
python3 -m venv .venv
. .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.text
```


# Testing/Verifying Solutions

Each day will include a pytest script that uses examples from the day.
This allows for verifying the code works by running `pytest`. For example:


Note: `--durations=0` shows the slowest tests (if taking longer then 0.005s). This is great for testing differences between changes.

```
|--% pytest -v --durations=0 puzzles/test_day01.py
============================================= test session starts ==============================================
platform linux -- Python 3.10.8, pytest-7.2.0, pluggy-1.0.0 -- /home/rreed/tmp/venv-advent-of-code/bin/python
cachedir: .pytest_cache
rootdir: 2022-advent-of-code
collected 4 items

puzzles/test_day01.py::test_example1 PASSED                                                              [ 25%]
puzzles/test_day01.py::test_example2 PASSED                                                              [ 50%]
puzzles/test_day01.py::test_part1 PASSED                                                                 [ 75%]
puzzles/test_day01.py::test_part2 PASSED                                                                 [100%]

============================================== slowest durations ===============================================
0.10s call     puzzles/test_day01.py::test_part2
0.06s call     puzzles/test_day01.py::test_part1

(10 durations < 0.005s hidden.  Use -vv to show these durations.)
============================================== 4 passed in 0.23s ===============================================
```
