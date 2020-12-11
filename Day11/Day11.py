import copy


def checkNeigbhors(map, x, y):
    count = 0
    if data[y-1][x-1] == '#':
        count += 1
    if data[y-1][x] == '#':
        count += 1
    if data[y-1][x+1] == '#':
        count += 1
    if data[y][x - 1] == '#':
        count += 1
    if data[y][x + 1] == '#':
        count += 1
    if data[y+1][x-1] == '#':
        count += 1
    if data[y+1][x] == '#':
        count += 1
    if data[y+1][x+1] == '#':
        count += 1
    return count


def checkDistantNeighbors(map, x, y):
    count = 0

    intx = x
    inty= y - 1
    while not map[inty][intx] == '|':
        if map[inty][intx] == '#':
            count += 1
            break
        if map[inty][intx] == 'L':
            break
        inty -= 1

    intx = x + 1
    inty = y - 1
    while not map[inty][intx] == '|':
        if map[inty][intx] == '#':
            count += 1
            break
        if map[inty][intx] == 'L':
            break
        inty -= 1
        intx += 1

    intx = x + 1
    inty = y
    while not map[inty][intx] == '|':
        if map[inty][intx] == '#':
            count += 1
            break
        if map[inty][intx] == 'L':
            break
        intx += 1

    intx = x + 1
    inty = y + 1
    while not map[inty][intx] == '|':
        if map[inty][intx] == '#':
            count += 1
            break
        if map[inty][intx] == 'L':
            break
        intx += 1
        inty += 1

    intx = x
    inty = y + 1
    while not map[inty][intx] == '|':
        if map[inty][intx] == '#':
            count += 1
            break
        if map[inty][intx] == 'L':
            break
        inty += 1

    intx = x - 1
    inty = y + 1
    while not map[inty][intx] == '|':
        if map[inty][intx] == '#':
            count += 1
            break
        if map[inty][intx] == 'L':
            break
        intx -= 1
        inty += 1

    intx = x - 1
    inty = y
    while not map[inty][intx] == '|':
        if map[inty][intx] == '#':
            count += 1
            break
        if map[inty][intx] == 'L':
            break
        intx -= 1

    intx = x - 1
    inty = y - 1
    while not map[inty][intx] == '|':
        if map[inty][intx] == '#':
            count += 1
            break
        if map[inty][intx] == 'L':
            break
        intx -= 1
        inty -= 1

    return count



def load(filename):
    data = []
    length = 0
    height = 0
    with open(filename) as file:
        data.append([])
        for y, line in enumerate(file):
            dataline = line.strip('\n')
            length = len(line) + 2
            if y == 0:
                for n in dataline:
                    data[0].append('|')
                data[0].append('|')
                data[0].append('|')
                data.append([])
            data[y+1].append('|')
            for x, pos in enumerate(dataline):
                data[y+1].append(pos)
            data[y+1].append('|')
            data.append([])
            height = y + 1
        for n in range(length):
            data[height + 1].append('|')
    return data

data = load("day11.txt")
print(data)
n = 0
stateChanged = False
dataCopy = copy.deepcopy(data)
while True:
    n+=1
    for y, row in enumerate(data):
        for x, pos in enumerate(row):
            if pos == 'L' and checkNeigbhors(data, x, y) == 0:
                #print('#', end='')
                dataCopy[y][x] = '#'
                stateChanged = True
            elif pos == '#' and checkNeigbhors(data, x, y) >= 4:
                #print('L', end='')
                dataCopy[y][x] = 'L'
                stateChanged = True
            #else:
                #print(pos, end='')
        #print()
    #print()
    if not stateChanged:
        break
    data = copy.deepcopy(dataCopy)
    stateChanged = False
print(data)
print(dataCopy)
count = 0
for n in data:
    for i in n:
        if i == '#':
            count += 1
print("Count: " + str(count))

# Part 2
data = load("day11.txt")
n = 0
stateChanged = False
dataCopy = copy.deepcopy(data)
while True:
    n+=1
    for y, row in enumerate(data):
        for x, pos in enumerate(row):
            if pos == 'L' and checkDistantNeighbors(data, x, y) == 0:
                # print('#', end='')
                dataCopy[y][x] = '#'
                stateChanged = True
            elif pos == '#' and checkDistantNeighbors(data, x, y) >= 5:
                # print('L', end='')
                dataCopy[y][x] = 'L'
                stateChanged = True
            #else:
               # print(pos, end='')
        #print()
    #print()
    if not stateChanged:
        break
    data = copy.deepcopy(dataCopy)
    stateChanged = False
print(data)
print(dataCopy)
count = 0
for n in data:
    for i in n:
        if i == '#':
            count += 1
print("Count: " + str(count))

