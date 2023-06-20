from tasks.Aoc6 import Aoc6
import unittest

class TestAoc6(unittest.TestCase):
    def test_solution(self):
        
        with self.subTest():
            input = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
            
            solution = Aoc6(input)

            assert solution.solution(4) == 7

        with self.subTest():
            input = "bvwbjplbgvbhsrlpgdmjqwftvncz"
            
            solution = Aoc6(input)

            assert solution.solution(4) == 5

    def test_solution_2(self):
        input = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
            
        solution = Aoc6(input)

        assert solution.solution(14) == 19
