from aocd import get_data

class Aoc4:
    def __init__(self, input):
        self.input = self._sanitize_input(input)

    def _sanitize_input(self, input):
        return [list(map(int, item.replace('-',',').split(','))) for item in input.strip().split("\n")]

    def solution(self):
        score = 0
        for item in self.input:
            if item[0] == item[2]:
                if item[1] == item[3]:
                    score += 1
                elif item[1] > item[3]:
                    if (item[0] <= item[2] <= item[1]) and (item[0] <= item[3] <= item[1]):
                        score += 1
                else:
                    if (item[2] <= item[0] <= item[3]) and (item[2] <= item[1] <= item[3]):
                        score += 1
            elif item[0] < item[2]:
                if (item[0] <= item[2] <= item[1]) and (item[0] <= item[3] <= item[1]):
                    score += 1

            else:
                if (item[2] <= item[0] <= item[3]) and (item[2] <= item[1] <= item[3]):
                    score += 1

        return score

    def solution_extra(self):
        score = 0
        for item in self.input:
            range1 = []
            range2 = []
            if item[0] == item[2]:
                if item[1] < item[3]:
                    range1 = range(item[2],item[3]+1)
                    range2 = range(item[0],item[1]+1)
                else:
                    range1 = range(item[0],item[1]+1)
                    range2 = range(item[2],item[3]+1)
            elif item[0] < item[2]:
                range1 = range(item[0],item[1]+1)
                range2 = range(item[2],item[3]+1)
            else:
                range1 = range(item[2],item[3]+1)
                range2 = range(item[0],item[1]+1)
            # if range1.start in range2 and range1[-1] in range2:
            #     score += 1
            if set(range2).issubset(range1):
                score += 1

        return score

    def solution_very_extra(self):
        score = 0
        for item in self.input:
            if item[0] <= item[2] and item[1] >= item[3] or item[2] <= item[0] and item[3] >= item[1]:
                score += 1
        return score

    def solution_2(self):
        score = 0
        for item in self.input:
            range1 = range(item[0],item[1]+1)
            range2 = range(item[2],item[3]+1)
            range1_set = set(range1)
            if range1_set.intersection(range2):
                score += 1

        return score

    def solution_2_extra(self):
        score = 0
        for item in self.input:
            if (item[0] <= item[2] or item[1] >= item[3]) and (item[2] <= item[0] or item[3] >= item[1]):
                score +=1
            # if (item[0] <= item[2] <= item[1]) or (item[0] <= item[3] <= item[1]) or (item[2] <= item[0] <= item[3]) or (item[2] <= item[1] <= item[3]):
            #     score += 1

        return score

def main():
    solution = Aoc4(get_data())
    print(solution.solution_very_extra())
    print(solution.solution_2_extra())

if __name__ == "__main__":
    main()