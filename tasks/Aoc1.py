from aocd import get_data

import functools

class Aoc1:
    def __init__(self, input):
        self.input = self._sanitize_input(input)

    def solution(self):
        ''' [[1000,2000],[3000]] ->  [3000,3000] '''
        return max(functools.reduce(lambda x, y : x+y, item) 
                        for item in self.input)

    def solution_2(self):
        sorted_list = sorted((functools.reduce(lambda x, y : x+y, item) 
                        for item in self.input), reverse=True)

        return sum(sorted_list[0:3])

    def _sanitize_input(self, input):
        ''' \'1000/n2000/n/n3000\' -> [[1000,2000],[3000]] '''
        return (map(int, item.split('\n')) for item in input.split("\n\n"))

def main():
    solution = Aoc1(get_data())
    print(solution.solution())
    print(solution.solution_2())

if __name__ == "__main__":
    main()