import re


def push(obj, l, depth):
    #print(depth)
    while depth:
        l = l[-1]
        depth -= 1

    l.append(obj)


def parse_parentheses(s):
    groups = []
    depth = 0

    try:
        for char in s:
            #print(groups)
            if char == '(':
                push([], groups, depth)
                depth += 1
            elif char == ')':
                depth -= 1
            elif char != ' ':
                push(char, groups, depth)
    except IndexError:
        raise ValueError('Parentheses mismatch')

    if depth > 0:
        raise ValueError('Parentheses mismatch')
    else:
        return groups


def load(filename):
    data = []
    with open(filename) as file:
        for line in file:
            dataline = line.strip("\n")

            parts = parse_parentheses(dataline)
            #for x, part in enumerate(parts):
                #part = part.split(' ')
               # parts[x] = part
            data.append(parts)
    return data


def loadPart2(filename):
    data = []
    with open(filename) as file:
        for line in file:
            dataline = line.strip("\n")
            dataline = dataline.replace('(', '((')
            dataline = dataline.replace(')', '))')
            dataline = dataline.replace('*', ')*(')
            dataline = '(' + dataline + ')'
            parts = parse_parentheses(dataline)


            data.append(parts)
    return data

def solveEquation(equation):
    #print("Equation:  " + str(equation))
    solution = 0
    operator = '_'
    if equation[0] == '*':
        solution = 1
    for part in equation:
        #print("Part: " + str(part))
        for subpart in part:
            if subpart == '':
                part.remove('')
        if not part == []:

            while True:
                #print(part)
                if not type(part) is list or len(part) > 1:
                    break
                part = part[0]
            if len(part) > 1:
                intermediate_answer = solveEquation(part)
                #print("1: " + str(solution) + "  " + operator + "    " + str(intermediate_answer))
                #if intermediate_answer[1] != '_':
                   # operator = intermediate_answer[1]

                if operator == '+':
                    solution += intermediate_answer[0]
                elif operator == '*':
                    solution *= intermediate_answer[0]
                else:
                    solution = intermediate_answer[0]
                #print("2: " + str(solution) + "  " + operator)
            else:
                # while True:
                #     print(part)
                #     if not type(part) is list or len(part) > 1:
                #         break
                #     part = part[0]


                if part == '*':
                    operator = '*'
                elif part == '+':
                    operator = '+'
                else:
                    if operator == '*':
                        solution *= int(part)
                    elif operator == '+':
                        solution += int(part)
                    else:
                        solution = int(part)
                    operator = '_'
    if equation[0] == '*':
        operator = '*'
    elif equation[0] == '+':
        operator = '+'

    #print(str(solution) + "   " + operator)
    return solution, operator


#Part 1

data = load("day18.txt")

total_sum = 0
for equation in data:
    #print(equation)
    value = solveEquation(equation)[0]
    #print(value)
    total_sum += value
print("answer part 1: " + str(total_sum))

# Part 2
data = loadPart2("day18.txt")

total_sum = 0
for equation in data:
    #print(equation)
    value = solveEquation(equation)[0]
    #print(value)
    total_sum += value
print("answer part 2: " + str(total_sum))

#print(total_sum)