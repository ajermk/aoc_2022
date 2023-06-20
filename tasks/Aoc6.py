from aocd import get_data

class Aoc6:
    def __init__(self, input):
        self.input = input
        self.input_length = len(self.input)

    def solution(self, window):
        for i in range(0,self.input_length - window + 1):
            subset = self.input[i:i + window]
            if len(subset) == len(set(subset)):
                return i + window

def main():
    solution = Aoc6(get_data())
    print(solution.solution(4))
    print(solution.solution(14))

if __name__ == "__main__":
    main()
