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


def rotateWaypoint(pos, degrees):
    quadrant = 0
    if pos[0] > 0 and pos[1] > 0:
        quadrant = 0
    if pos[0] > 0 and pos[1] < 0:
        quadrant = 1
    if pos[0] < 0 and pos[1] < 0:
        quadrant = 2
    if pos[0] < 0 and pos[1] > 0:
        quadrant = 3

    if quadrant == 1 or quadrant == 3:
        temp = pos[0]
        pos[0] = pos[1]
        pos[1] = temp

    steps = int(degrees/90)
    ind = divmod(quadrant + steps, 4)[1]
    # print("quad: " + str(quadrant))
    if ind == 0:
        newPos = [abs(pos[0]), abs(pos[1])]
    if ind == 1:
        newPos = [abs(pos[1]), -abs(pos[0])]
    if ind == 2:
        newPos = [-abs(pos[0]), -abs(pos[1])]
    if ind == 3:
        newPos = [-abs(pos[1]), abs(pos[0])]
    # print(str(newPos) + str(ind))
    return newPos


def moveToWaypoint(pos, waypoint, units):
    newpos = pos
    newpos[0] = newpos[0] + waypoint[0] * units
    newpos[1] = newpos[1] + waypoint[1] * units
    return newpos


data = load("day12.txt")
print(data)

pos = [0, 0]
directions = ['E', 'S', 'W', 'N']
currentDirection = 'E'

# Part 1

for d in data:
    # print(d[0] + " " + d[1])
    if d[0] == 'F':
       pos = moveForward(currentDirection, pos, d[1])
    elif d[0] == 'R':
        currentDirection = rotate(currentDirection, int(d[1]))
    elif d[0] == 'L':
        currentDirection = rotate(currentDirection, -int(d[1]))
    else:
        pos = moveForward(d[0], pos, d[1])
    # print(str(pos) + "  " + currentDirection)

print(pos)
print("Part 1 Manhattan: " + str(abs(pos[0]) + abs(pos[1])))


# Part 2
pos = [0, 0]
waypoint = [10, 1]

for d in data:
    # print(d[0] + " " + d[1])
    if d[0] == 'F':
       pos = moveToWaypoint(pos, waypoint, int(d[1]))
    elif d[0] == 'R':
        waypoint = rotateWaypoint(waypoint, int(d[1]))
    elif d[0] == 'L':
        waypoint = rotateWaypoint(waypoint, -int(d[1]))
    else:
        waypoint = moveForward(d[0], waypoint, d[1])
    # print(str(pos) + "  " + " " + str(waypoint))


print(pos)
print("Part 2 Manhattan: " + str(abs(pos[0]) + abs(pos[1])))



