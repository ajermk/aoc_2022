from tasks.Aoc1 import Aoc1
import unittest

class TestAoc1(unittest.TestCase):
    def test_solution(self):
        solution = Aoc1(
            "1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000"
        )

        assert solution.solution() == 24000

    def test_input_sanitization(self):
        solution = Aoc1(
            "1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000"
        )

        solution2 = Aoc1(f"1000\n2000\n3000\n\n\
            4000\n5000\n6000\n\n7000\n\
                \n8000\n9000\n\n10000")

        generated = [list(item) for item in solution.input]

        assert generated == [[1000,2000,3000],[4000],[5000,6000],[7000,8000,9000],[10000]]

    def test_solution_2(self):
        solution = Aoc1(
            "1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000"
        )
        solution = solution.solution_2()
        assert solution == 45000
if __name__ == '__main__':
    unittest.main()