from tasks.Aoc3 import Aoc3
import unittest

class TestAoc3(unittest.TestCase):
    def test_solution(self):
        input = "vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\nPmmdzqPrVvPwwTWBwg\nwMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\nttgJtRGJQctTZtZT\nCrZsJsPPZsGzwwsLwLmpwMDw"
        solution = Aoc3(input)

        assert solution.solution() == 157

    def test_sanitize_input(self):
        input = "vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\nPmmdzqPrVvPwwTWBwg"
        solution = Aoc3(input)

        assert solution.input == [['vJrwpWtwJgWr', 'hcsFMMfFFhFp'], ['jqHRNqRjqzjGDLGL', 'rsFMfFZSrLrFZsSL'], ['PmmdzqPrV', 'vPwwTWBwg']]

    def test_intersection(self):
        input = "vJrwpWtwJgWrhcsFMMfFFhFp"
        solution = Aoc3(input)

        common_element = solution._find_common_element(solution.input[0][0],solution.input[0][1])

        assert common_element == 'p'

    def test_sanitize_input_2(self):
        input = "vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\nPmmdzqPrVvPwwTWBwg\nwMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\nttgJtRGJQctTZtZT\nCrZsJsPPZsGzwwsLwLmpwMDw"
        solution = Aoc3(input)

        assert list(solution.input) == [('vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg'),('wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw')]

    def test_intersection_2(self):
        input = "fcghj\nfnjkjikl\nfdserftghj"
        solution = Aoc3(input)

        list_version = list(solution.input)

        common_element = solution._find_common_element(list_version[0][0],*list_version[0][1:])

        assert common_element == 'f'

    def test_solution_2(self):
        input = "vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\nPmmdzqPrVvPwwTWBwg\nwMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\nttgJtRGJQctTZtZT\nCrZsJsPPZsGzwwsLwLmpwMDw"
        solution = Aoc3(input)

        assert solution.solution_2() == 70