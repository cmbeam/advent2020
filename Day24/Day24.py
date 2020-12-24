def load(filename):
    data = []
    with open(filename) as file:
        for line in file:
            data_line = line.strip("\n")
            data .append(data_line)
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


data = load('day24.txt')


size = 50
grid = [[0 for y in range(size)] for x in range(size)]

for tile in data:
    coord = [int(size/2), int(size/2)]
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
    #print("Tile coord: " + str(coord))
    if grid[coord[0]][coord[1]] == 1:
        grid[coord[0]][coord[1]] = 0
    else:
        grid[coord[0]][coord[1]] = 1

count = 0
for line in grid:
    for pos in line:
        #print(pos, end='')
        if pos == 1:
            count += 1
    #print()

print("Answer part 1: " + str(count))




