def load(filename):
    data = []
    with open(filename) as file:
        for x, line in enumerate(file):
            dataline = line.strip('\n')
            direction = [dataline[0], dataline[1:]]
            data.append(direction)
    return data

def moveForward(currentDirection, pos, units):
    newpos = []
    if currentDirection == 'W':
        newpos = [int(pos[0]) - int(units), int(pos[1])]
    if currentDirection == 'N':
        newpos = [int(pos[0]), int(pos[1]) + int(units)]
    if currentDirection == 'E':
        newpos = [int(pos[0]) + int(units), int(pos[1])]
    if currentDirection == 'S':
        newpos = [int(pos[0]), int(pos[1]) - int(units)]
    return newpos

def rotate(direction, degrees):
    steps = int(degrees/90)
    ind = directions.index(direction)
    #print(str(degrees) + " " + str(ind) + " " + str(steps))

    ind = divmod(ind + steps, 4)[1]
    #print(str(steps) + " " + direction + str(ind) + " " + directions[ind])
    newD = directions[ind]
    return newD

data = load("day12.txt")
print(data)

pos = [0, 0]
directions = ['E', 'S', 'W', 'N']
currentDirection = 'E'

# Part 1

print(pos)
for d in data:
    print(d[0] + " " + d[1])
    if d[0] == 'F':
       pos = moveForward(currentDirection, pos, d[1])
    elif d[0] == 'R':
        currentDirection = rotate(currentDirection, int(d[1]))
    elif d[0] == 'L':
        currentDirection = rotate(currentDirection, -int(d[1]))
    else:
        pos = moveForward(d[0], pos, d[1])
    print(str(pos) + "  " + currentDirection)


print(pos)
print("Manhattan: " + str(abs(pos[0]) + abs(pos[1])))


# Part 2
print(pos)
for d in data:
    print(d[0] + " " + d[1])
    if d[0] == 'F':
       pos = moveForward(currentDirection, pos, d[1])
    elif d[0] == 'R':
        currentDirection = rotate(currentDirection, int(d[1]))
    elif d[0] == 'L':
        currentDirection = rotate(currentDirection, -int(d[1]))
    else:
        pos = moveForward(d[0], pos, d[1])
    print(str(pos) + "  " + currentDirection)


print(pos)
print("Manhattan: " + str(abs(pos[0]) + abs(pos[1])))



