class Instruction:
    def __init__(self, operation, argument):
        self.operation = operation
        self.argument = argument


class Console:
    def __init__(self, code):
        self.code = code
    accumulator = 0
    position = 0

    def run(self):
        register = [0 for j in range(len(self.code))]
        replacecount = -1
        counter = 0
        while self.position < len(code):
            if register[self.position] == 1:
                if replacecount == -1:
                    print("Part 1 Answer: " + str(self.accumulator))
                else:
                    print("Infinite loop.   Interrupted  Accumulator: " + str(self.accumulator))
                self.position = 0
                self.accumulator = 0
                register = [0 for j in range(len(code))]
                replacecount += 1
                counter = 0
            else:
                register[self.position] = 1
                operation = code[self.position].operation
                if operation == 'nop':
                    if counter == replacecount:
                        operation = 'jmp'
                    else:
                        self.position += 1
                    counter += 1
                if operation == 'acc':
                    number = code[self.position].argument
                    self.accumulator = self.accumulator + int(number)
                    self.position += 1
                if operation == 'jmp':
                    if counter == replacecount:
                        self.position += 1
                    else:
                        number = code[self.position].argument
                        self.position = self.position + int(number)
                    counter += 1
        print("Part 2 Answer: " + str(self.accumulator))

def load(filename):
    instructions = {}
    with open(filename) as file:
        for x, line in enumerate(file):
            instruction = Instruction(line[:3], int(line[4:]))
            instructions[x] = instruction
    return instructions


code = load("Day8/day8.txt")
console = Console(code)
console.run()

