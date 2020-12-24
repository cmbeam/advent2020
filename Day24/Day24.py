import json


def load(filename):
    data = []
    with open(filename) as file:
        for line in file:
            data_line = line.strip("\n")
            data.append(data_line)
    return data


def move_sw(coord):
    if divmod(coord[1], 2)[1] == 0:
        coord[0] -= 1
    coord[1] += 1
    return coord


def move_se(coord):
    if divmod(coord[1], 2)[1] == 1:
        coord[0] += 1
    coord[1] += 1
    return coord


def move_nw(coord):
    if divmod(coord[1], 2)[1] == 0:
        coord[0] -= 1
    coord[1] -= 1
    return coord


def move_ne(coord):
    if divmod(coord[1], 2)[1] == 1:
        coord[0] += 1
    coord[1] -= 1
    return coord


def move_e(coord):
    coord[0] += 1
    return coord


def move_w(coord):
    coord[0] -= 1
    return coord


def neighbor_count(grid, pos):
    count = 0
    coord = json.loads(pos)
    if divmod(coord[1], 2)[1] == 1:
        if str([coord[0], coord[1] - 1]) in grid and grid[str([coord[0], coord[1] - 1])] == 1:
            count += 1
        if str([coord[0] + 1, coord[1] - 1]) in grid and grid[str([coord[0] + 1, coord[1] - 1])] == 1:
            count += 1
        if str([coord[0] + 1, coord[1]]) in grid and grid[str([coord[0] + 1, coord[1]])] == 1:
            count += 1
        if str([coord[0] + 1, coord[1] + 1]) in grid and grid[str([coord[0] + 1, coord[1] + 1])] == 1:
            count += 1
        if str([coord[0], coord[1] + 1]) in grid and grid[str([coord[0], coord[1] + 1])] == 1:
            count += 1
        if str([coord[0] - 1, coord[1]]) in grid and grid[str([coord[0] - 1, coord[1]])] == 1:
            count += 1
    else:
        if str([coord[0] - 1, coord[1] - 1]) in grid and grid[str([coord[0] - 1, coord[1] - 1])] == 1:
            count += 1
        if str([coord[0], coord[1] - 1]) in grid and grid[str([coord[0], coord[1] - 1])] == 1:
            count += 1
        if str([coord[0] + 1, coord[1]]) in grid and grid[str([coord[0] + 1, coord[1]])] == 1:
            count += 1
        if str([coord[0], coord[1] + 1]) in grid and grid[str([coord[0], coord[1] + 1])] == 1:
            count += 1
        if str([coord[0] - 1, coord[1] + 1]) in grid and grid[str([coord[0] - 1, coord[1] + 1])] == 1:
            count += 1
        if str([coord[0] - 1, coord[1]]) in grid and grid[str([coord[0] - 1, coord[1]])] == 1:
            count += 1
    return count


data = load('day24.txt')

grid = {}

for tile in data:
    coord = [5, 5]
    step = ''
    for next_char in tile:
        step += next_char
        if not (step == 's' or step == 'n'):
            if step == 'e':
                coord = move_e(coord)
            elif step == 'w':
                coord = move_w(coord)
            elif step == 'nw':
                coord = move_nw(coord)
            elif step == 'ne':
                coord = move_ne(coord)
            elif step == 'sw':
                coord = move_sw(coord)
            elif step == 'se':
                coord = move_se(coord)
            step = ''
    if str(coord) in grid and grid[str(coord)] == 1:
        grid[str(coord)] = 0
    else:
        grid[str(coord)] = 1

count = 0
# for pos in grid:
#     print(pos + " " + str(grid[pos]), end=' : ')
#     if grid[pos] == 1:
#         count += 1
print()
print("Answer part 1: " + str(count))

# Part 2
size = 100
for n in range(100):
    next_grid = {}
    for y in range(-size, size+1):
        # if divmod(y,2)[1] == 1:
        #     print(' ',end='')
        for x in range(-size, size+1):
            pos = str([x, y])
            if pos in grid and grid[pos] == 1:
                if neighbor_count(grid, pos) == 0 or neighbor_count(grid, pos) > 2:
                    next_grid[pos] = 0
                else:
                     next_grid[pos] = 1
                #print('# ', end='')
                # print(neighbor_count(grid, pos), end=' ')
            else:
                if neighbor_count(grid, pos) == 2:
                    next_grid[pos] = 1
                #print('. ', end='')
                #print(neighbor_count(grid, pos), end=' ')
        # print(y)
    grid = next_grid.copy()

    count = 0
    for pos in grid:
        #print(pos + " " + str(grid[pos]) , end=' : ')
        if grid[pos] == 1:
            count += 1
    # print()
    # print("Day " + str(n+1) + " count: " + str(count))

print("Answer part 2: " + str(count))
