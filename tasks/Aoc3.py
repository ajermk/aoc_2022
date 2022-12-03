from aocd import get_data

class Aoc3:
    def __init__(self, input):
        self.input = self._sanitize_input(input) # change to _sanitize_input for first solution

    def _sanitize_input(self, input):
        ''' String with newline symbols -> divide single line into two strings eg [['str','ing'], [...], [...]]'''
        return [[item[:len(item)//2], item[len(item)//2:]] for item in input.strip().split("\n")]

    def _sanitize_input_2(self, input):
        ''' String with newline symbols -> 
        
        Each 3 lines into a single set, eg:
        [('string', 'string2', 'strin3'), (...), ...] 
        
        '''
        initial_list = [item for item in input.strip().split("\n")]
        grouping_size = 3
        return zip(*(iter(initial_list),) * grouping_size)

    def _find_common_element(self, input1, *args):
        common_element = set(input1).intersection(*args)
        return next(iter(common_element))

    def solution(self):
        score = 0
        for item in self.input:
            common_element = self._find_common_element(item[0], *item[1:])
            if common_element.islower():
                score += ord(common_element) - 96
            elif common_element.isupper():
                score += ord(common_element) - 38

        return score

def main():
    solution = Aoc3(get_data())
    # print(solution.solution())
    print(solution.solution_2())

if __name__ == "__main__":
    main()