def load(filename):
    data = {}
    with open(filename) as file:
        for x, line in enumerate(file):
            data[x] = line.strip('\n')
    return data

def checkValid(block, number):
    count = 0
    for x in block:
        x = int(x)
        for y in block[count + 1:]:
            y = int(y)
            # print("x: " + str(x) + " y: " + str(y) + " sum: " + str(x+y) + " Number: " + str(number))
            if x != y and x + y == number:
                return True
        count += 1
    return False

def addToBlock(block, number):
    newBlock = [0 for j in range(25)]
    for x, blocknumber in enumerate(block):
        if x > 0:
            newBlock[x-1] = blocknumber
    newBlock[24] = number
    return newBlock

def findContiguous(block, number):
    count = 0

    for x in block:
        x = int(x)
        sum = x
        smallest = x
        largest = x
        for y in block[count + 1:]:
            y = int(y)
            sum = sum + y
            if y < smallest:
                smallest = y
            if y > largest:
                largest = y
            print(str(sum) + " " + number)
            if sum == int(number):
                print("done  smallest: " + str(smallest) + " largest: " + str(largest) + " sum: " + str(smallest + largest))

                return True
        count += 1
    return False

data = load("Day9/day9.txt")

wholeblock = [0 for j in range(len(data))]
for x in data:
    wholeblock[x] = data[x]
print(wholeblock)
currentblock = [0 for j in range(25)]
for x in data:
    if x < 25:
        currentblock[x] = data[x]

for x in data:
    if x > 24:
        print(data[x])
        print(currentblock)
        if not checkValid(currentblock, int(data[x])):
            print("First Invalid: " + str(data[x]))
            findContiguous(wholeblock, data[x])
            break
        currentblock = addToBlock(currentblock, data[x])
