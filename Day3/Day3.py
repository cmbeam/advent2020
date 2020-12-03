# Load file
def loadpuzzle(file):
    grid = [[0 for i in range(31)] for j in range(323)]
    puzzle = open(file, 'r')
    y = 0
    for line in puzzle:
        x = 0
        for obstacle in line:
            if obstacle != '\n':
                grid[y][x] = obstacle
            x = x + 1
        y = y + 1
    print(grid)
    return grid





def traversegrid(grid, slopeX, slopeY):
    treeCount = 0
    x = slopeX
    y = slopeY


    while y < 323:
        if grid[y][x] == '#':
            print('hit: ' + str(x) + " " + str(y))
            treeCount = treeCount + 1
        else:
            print('miss: ' + str(x) + " " + str(y))
        y=y+slopeY
        x=x+slopeX
        if x > 30:
            x = x - 31
    return treeCount


file = 'Day3/day3.txt'
grid = loadpuzzle(file)

# part 1
print(traversegrid(grid, 3, 1))

# part 2
answer = traversegrid(grid, 1, 1) * traversegrid(grid, 3, 1) * traversegrid(grid, 5, 1) * traversegrid(grid, 7, 1) * traversegrid(grid, 1, 2)
print(answer)
