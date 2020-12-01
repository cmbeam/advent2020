from itertools import permutations
import time

puzzleInput = []
file = open('Day1/day1.txt', 'r')
for entry in file:
    puzzleInput.append(int(entry))

# Part 1
answer1 = 0

start = time.perf_counter()
perm = permutations(puzzleInput, 2)
for i in list(perm):
    sum = i[0] + i[1]
    if sum == 2020:
        answer1 = i[0] * i[1]
print(answer1)
stop = time.perf_counter()
print(f"Time: {stop - start:0.4f}")


start = time.perf_counter()
for x in range(0, len(puzzleInput)):
    for y in range(x+1, len(puzzleInput)):
        sum = puzzleInput[x] + puzzleInput[y]
        if sum == 2020:
            answer1 = puzzleInput[x] * puzzleInput[y]

print(answer1)
stop = time.perf_counter()
print(f"Time: {stop - start:0.4f}")

# Part 2
answer2 = 0

start = time.perf_counter()
perm = permutations(puzzleInput, 3)
for i in list(perm):
    sum = i[0] + i[1] + i[2]
    if sum == 2020:
        answer2 = i[0] * i[1] * i[2]

print(answer2)
stop = time.perf_counter()
print(f"Time: {stop - start:0.4f}")

start = time.perf_counter()
for x in range(0, len(puzzleInput)):
    for y in range(x+1, len(puzzleInput)):
        for z in range(0, len(puzzleInput)):
            if z != x & z != y:
                sum = puzzleInput[x] + puzzleInput[y] + puzzleInput[z]
                if sum == 2020:
                    answer2 = puzzleInput[x] * puzzleInput[y] * puzzleInput[z]

print(answer2)
stop = time.perf_counter()
print(f"Time: {stop - start:0.4f}")
