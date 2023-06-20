import re
from aocd import get_data

class Aoc5:
    def __init__(self,input=None):
        if input:
            self.stacks, self.instructions = self._sanitize_input(input)

    def _sanitize_input(self, input):
        ascii, instructions = input.split("\n\n")
        
        parsed_ascii = []
        for line in ascii.split("\n"):
            if "1" in line:
                continue
            new_line = []
            for character in line[1::4]:
                if character == " ":
                    new_line.append("-")
                else:
                    new_line.append(character)
            parsed_ascii.insert(0, new_line)

        stacks = self._create_stacks(parsed_ascii)
        numbered_instructions = self._store_instructions(instructions)

        return stacks, numbered_instructions

    def _create_stacks(self, parsed_ascii):
        count_of_stacks = len(parsed_ascii[0])
        stacks = [[] for _ in range(count_of_stacks)]

        for line in parsed_ascii:
            for i, character in enumerate(line):
                if character != '-':
                    stacks[i].append(character)

        return stacks

    def _store_instructions(self, instructions):
        numbered_instructions = []
        for line in instructions.split("\n"):
            numbered_instructions.append([int(nums) for nums in re.findall(r'\b\d+\b', line)])

        return numbered_instructions

    def solution(self):
        for instruction in self.instructions:
            for _ in range(instruction[0]):
                self.stacks[instruction[2]-1].append(self.stacks[instruction[1]-1].pop())
        solution = ""
        for stack in self.stacks:
            solution += str(stack[-1])
        return solution

    def solution_2(self):
        for instruction in self.instructions:
            pop_position = len(self.stacks[instruction[1]-1]) - instruction[0]
            for _ in range(instruction[0]):
                self.stacks[instruction[2]-1].append(self.stacks[instruction[1]-1].pop(pop_position))
        solution = ""
        for stack in self.stacks:
            solution += str(stack[-1])
        return solution

def main():
    solution = Aoc5(get_data())
    #print(solution.solution())
    print(solution.solution_2())

if __name__ == "__main__":
    main()
