from tasks.Aoc4 import Aoc4
import unittest

class TestAoc4(unittest.TestCase):
    def test_solution(self):
        input = "2-4,6-8\n2-3,4-5\n5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8"

        solution = Aoc4(input)

        assert solution.solution_extra() == 2

    def test_sanitize_input(self):
        input = "2-4,6-8\n2-3,4-5\n5-7,7-9"

        solution = Aoc4(input)

        #generated = [list(item) for item in solution.input]


        assert solution.input == [[2,4,6,8],[2,3,4,5],[5,7,7,9]]

    
    def test_solution_2(self):
        input = "2-4,6-8\n2-3,4-5\n5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8"

        solution = Aoc4(input)

        assert solution.solution_2_extra() == 4