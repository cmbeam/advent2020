class Instruction:
    def __init__(self, operation, argument):
        self.operation = operation
        self.argument = argument


def load(filename):
    instructions = {}
    with open(filename) as file:
        for x, line in enumerate(file):
            instruction = Instruction(line[:3], int(line[4:]))
            instructions[x] = instruction
    return instructions


code = load("Day8/day8.txt")
print(code)

accumulator = 0
marker = 0
register = [0 for j in range(len(code))]
replacecount = -1
counter = 0

while marker < len(code):
    if register[marker] == 1:
        if replacecount == -1:
            print("Part 1 Answer: " + str(accumulator))
        else:
            print("Infinite loop.   Interupted  Accumulator: " + str(accumulator))
        marker = 0
        accumulator = 0
        register = [0 for j in range(len(code))]
        replacecount = replacecount + 1
        counter = 0
    else:
        register[marker] = 1
        operation = code[marker].operation
        if operation == 'nop':
            if counter == replacecount:
                operation = 'jmp'
            else:
                marker = marker + 1
            counter = counter + 1
        if operation == 'acc':
            number = code[marker].argument
            accumulator = accumulator + int(number)
            marker = marker + 1
        if operation == 'jmp':
            if counter == replacecount:
                marker = marker + 1
            else:
                number = code[marker].argument
                marker = marker + int(number)
            counter = counter + 1

print("Part 2 Answer: " + str(accumulator))
