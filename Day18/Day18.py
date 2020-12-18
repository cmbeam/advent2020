import re

def load(filename):
    data = []
    with open(filename) as file:
        for line in file:
            dataline = line.strip("\n")
            parts = re.split('\(|\)', dataline)
            for x, part in enumerate(parts):
                part = part.split(' ')
                parts[x] = part
            data.append(parts)
    return data

def solveEquation(equation):
    print("Equation:  " + str(equation))
    solution = 0
    operator = '_'
    if equation[0] == '*':
        solution = 1
    for part in equation:
        print("Part: " + str(part))
        for subpart in part:
            if subpart == '':
                part.remove('')
        if not part == []:

            if len(part) > 1:
                intermediate_answer = solveEquation(part)
                print("1: " + str(solution) + "  " + operator + "    " + str(intermediate_answer))
                if intermediate_answer[1] != '_':
                    operator = intermediate_answer[1]

                if operator == '+':
                    solution += intermediate_answer[0]
                elif operator == '*':
                    solution *= intermediate_answer[0]
                else:
                    solution = intermediate_answer[0]
                #print("2: " + str(solution) + "  " + operator)
            else:
                for singlepart in part:
                    part = singlepart
                    break
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

data = load("day18test.txt")
#print(data)

total_sum = 0
for equation in data:
    print(equation)
    value = solveEquation(equation)[0]
    print(value)
    total_sum += value
print("anser: " + str(total_sum))

#print(total_sum)