def loadpuzzle(file):
    instructions = {}
    x = 0
    with open(file) as puzzle:
        for line in puzzle:
            instruction = {}
            operation = line.split(' ')[0]
            argument = line.split(' ')[1]
            number = argument[1:]
            sign = argument[0]
            instruction[0] = operation
            instruction[1] = sign
            instruction[2] = number
            instructions[x] = instruction
            x = x + 1
    return instructions


code = loadpuzzle("Day8/day8.txt")
print(code)


accumulator = 0
marker = 0
register = [0 for j in range(len(code))]
run = True
replacecount = -1
counter = 0


while marker < len(code) and run:
    # print(str(marker + 1) + "  " + str(code[marker]))
    if register[marker] == 1:
        if replacecount == -1:
            print("Part 1 Answer: " + str(accumulator))
        else:
            print("Infinite loop.   Interupted  Accumulator: " + str(accumulator))
        # run = False
        marker = 0
        accumulator = 0
        register = [0 for j in range(len(code))]
        replacecount = replacecount + 1
        counter = 0
    else:
        register[marker] = 1

        operation = code[marker][0]
        if operation == 'nop':
            if counter == replacecount:
                operation = 'jmp'
            else:
                marker = marker + 1
            counter = counter + 1
        if operation == 'acc':
            sign = code[marker][1]
            number = code[marker][2]
            if sign == '+':
                accumulator = accumulator + int(number)
            else:
                accumulator = accumulator - int(number)
            marker = marker + 1
        if operation == 'jmp':
            if counter == replacecount:
                marker = marker + 1
            else:
                sign = code[marker][1]
                number = code[marker][2]
                if sign == '+':
                    marker = marker + int(number)
                else:
                    marker = marker - int(number)
            counter = counter + 1

print("Part 2 Answer: " + str(accumulator))
