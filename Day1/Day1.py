from itertools import combinations
import time


def loadpuzzle(file):
    puzzleInput = []
    file = open('Day1/day1.txt', 'r')
    for entry in file:
        puzzleInput.append(int(entry))
    return puzzleInput


def combo2(input):
    answer = 0
    start = time.perf_counter()
    perm = combinations(input, 2)
    for i in list(perm):
        sum = i[0] + i[1]
        if sum == 2020:
            answer = i[0] * i[1]
    stop = time.perf_counter()
    # print(f"Time: {stop - start:0.4f}")
    return answer


def bruteforce2(input):
    answer = 0
    start = time.perf_counter()
    for x in range(0, len(input)):
        for y in range(x+1, len(input)):
            sum = input[x] + input[y]
            if sum == 2020:
                answer = input[x] * input[y]

    stop = time.perf_counter()
    # print(f"Time: {stop - start:0.4f}")
    return answer


def combo3(input):
    answer = 0
    start = time.perf_counter()
    perm = combinations(input, 3)
    for i in list(perm):
        sum = i[0] + i[1] + i[2]
        if sum == 2020:
            answer = i[0] * i[1] * i[2]

    stop = time.perf_counter()
    # print(f"Time: {stop - start:0.4f}")
    return answer


def bruteforce3(input):
    answer = 0
    start = time.perf_counter()
    for x in range(0, len(input)):
        for y in range(x+1, len(input)):
            for z in range(0, len(input)):
                if z != x & z != y:
                    sum = input[x] + input[y] + input[z]
                    if sum == 2020:
                        answer = input[x] * input[y] * input[z]
    stop = time.perf_counter()
    # print(f"Time: {stop - start:0.4f}")
    return answer


# Load puzzle file
puzzleInput = loadpuzzle("Day1/day1.txt")

# Part 1
print("Part 1 with combinations: " + str(combo2(puzzleInput)))
print("Part 1 with brute force: " + str(bruteforce2(puzzleInput)))

# Part 2
print("Part 2 with combinations: " + str(combo3(puzzleInput)))
print("Part 2 with brute force: " + str(bruteforce3(puzzleInput)))