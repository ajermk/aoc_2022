from tasks.Aoc5 import Aoc5
import unittest

class TestAoc5(unittest.TestCase):
    def test_solution(self):
        pass

    def test_sanitize_input(self):
        input = "    [D]    \n[N] [C]    \n[Z] [M] [P]\n1   2   3 \n\nmove 1 from 2 to 1\nmove 3 from 1 to 3\nmove 2 from 2 to 1\nmove 1 from 1 to 2"

        solution = Aoc5()

        assert solution._sanitize_input(input) == "    [D]    \n[N] [C]    \n[Z] [M] [P]\n1   2   3 ", "move 1 from 2 to 1\nmove 3 from 1 to 3\nmove 2 from 2 to 1\nmove 1 from 1 to 2"

    def test_stack_creation(self):
        solution = Aoc5()

        input = [['Z', 'M', 'P'], ['N', 'C', '-'], ['-', 'D', '-']]

        assert solution._create_stacks(input) == [['Z','N'],['M','C','D'],['P']]

    def test_numbered_instructions(self):
        solution = Aoc5()

        input = "move 1 from 2 to 1\nmove 3 from 1 to 3\nmove 2 from 2 to 1\nmove 1 from 1 to 2"

        assert solution._store_instructions(input) == [[1,2,1],[3,1,3],[2,2,1],[1,1,2]]

    def test_solution(self):
        input = "    [D]    \n[N] [C]    \n[Z] [M] [P]\n1   2   3 \n\nmove 1 from 2 to 1\nmove 3 from 1 to 3\nmove 2 from 2 to 1\nmove 1 from 1 to 2"

        solution = Aoc5(input)

        assert solution.solution() == "CMZ"

    def test_solution_2(self):
        input = "    [D]    \n[N] [C]    \n[Z] [M] [P]\n1   2   3 \n\nmove 1 from 2 to 1\nmove 3 from 1 to 3\nmove 2 from 2 to 1\nmove 1 from 1 to 2"

        solution = Aoc5(input)

        assert solution.solution_2() == "MCD"