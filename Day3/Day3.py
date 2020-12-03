# Load file
def loadpuzzle(file):
    grid = [[0 for i in range(31)] for j in range(323)]
    with open(file) as puzzle:
        for y, line in enumerate(puzzle):
            line = line.strip('\n')
            for x, obstacle in enumerate(line):
                grid[y][x] = obstacle
    return grid


def traverse(grid, slopeX, slopeY):
    treecount = 0
    x = slopeX
    y = slopeY

    while y < 323:
        if grid[y][x] == '#':
            treecount = treecount + 1
        y = y + slopeY
        x = x + slopeX
        if x > 30:
            x = x - 31
    return treecount


# Load file
file = 'Day3/day3.txt'
grid = loadpuzzle(file)

# part 1
print(traverse(grid, 3, 1))

# part 2
answer = traverse(grid, 1, 1) * traverse(grid, 3, 1) * traverse(grid, 5, 1) *\
         traverse(grid, 7,1) * traverse(grid, 1, 2)
print(answer)
