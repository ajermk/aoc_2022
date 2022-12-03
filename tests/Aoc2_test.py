from tasks.Aoc2 import Aoc2
import unittest

class TestAoc2(unittest.TestCase):
    def test_solution(self):
        input = "A Y\nB X\nC Z"
        aoc2 = Aoc2(input)
        aoc2.solution() == 15

    def test_solution_2(self):
        input = "A Y\nB X\nC Z"
        aoc2 = Aoc2(input)
        aoc2.solution_2() == 12

    def test_sanitize_input(self):
        input = "A Y\nB X\nC Z"
        aoc2 = Aoc2(input)

        assert aoc2.input == [['A','Y'],['B','X'],['C','Z']]