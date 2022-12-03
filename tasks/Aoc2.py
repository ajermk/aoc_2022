from aocd import get_data

class Aoc2:
    def __init__(self, input) -> None:
        self.input = self._sanitize_input(input)
        self.rules = {
            1:3,
            2:1,
            3:2
        }

        self.losing = {
            1:2,
            2:3,
            3:1
        }


        self.converter = {
            'A':1,
            'B':2,
            'C':3,
            'X':1,
            'Y':2,
            'Z':3
        }

    def solution(self):
        score = 0
        for item in self.input:
            if self.converter[item[0]] == self.converter[item[1]]:
                score += 3
            elif self.rules[self.converter[item[1]]] == self.converter[item[0]]:
                score += 6
            score += self.converter[item[1]]

        return score

    def solution_2(self):
        score = 0
        for item in self.input:
            if item[1] == 'X':
                score += self.rules[self.converter[item[0]]] 
            elif item[1] == 'Y':
                score += self.converter[item[0]]
                score += 3
            elif item[1] == 'Z':
                score += self.losing[self.converter[item[0]]]
                score += 6

        return score

    def _sanitize_input(self, input):
        return [item.split(' ') for item in input.split("\n")]

def main():
    solution = Aoc2(get_data())
    #print(solution.solution())
    print(solution.solution_2())

if __name__ == "__main__":
    main()