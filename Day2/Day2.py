from itertools import permutations
import time

puzzleInput = []
count = 0
file = open('Day2/day2.txt', 'r')
for entry in file:
    part0 = entry.split('-')
    min = int(part0[0])
    part1 = part0[1].split(" ")
    max = int(part1[0])
    checkLetter = part1[1].split(":")[0]
    code = part1[2]

    letterCount = 0
    for letter in code:
        if letter == checkLetter:
            letterCount = letterCount + 1
    if min <= letterCount <= max:
        count = count + 1

print(count)
file.close()

# Part 2
count = 0
file = open('Day2/day2.txt', 'r')
for entry in file:
    part0 = entry.split('-')
    position1 = int(part0[0])
    part1 = part0[1].split(" ")
    position2 = int(part1[0])
    checkLetter = part1[1].split(":")[0]
    code = part1[2]

    letterCount = 0
    if code[position1-1] == checkLetter and code[position2-1] != checkLetter:
        count = count + 1
    if code[position1-1] != checkLetter and code[position2-1] == checkLetter:
        count = count + 1

print(count)

