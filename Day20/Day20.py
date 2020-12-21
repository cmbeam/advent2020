def borders(grid):
    borders = ['' for n in range(4)]
    border_strings = []
    links = []
    borders[0] = grid[0][0:]
    for line in grid:
        borders[1] = borders[1] + line[len(line) - 1]
    for line in reversed(grid):
        borders[3] = borders[3] + line[0]
    borders[2] = grid[-1][::-1]
    for border in borders:
        border_string = ""
        for n in border:
            border_string = border_string + n
            link = '0'
        border_strings.append(border_string)
        links.append('')

    return border_strings, links


def rotate(tile):
    print("rotate")
    grid = tile[1]
    new_grid = [[] for i in range(len(grid))]
    for line in reversed(grid):
        for x in range(len(line)):
            new_grid[x].append(line[x])
    tile[1] = new_grid

    links = tile[2]
    new_links = [[] for n in range(2)]
    new_links[0].append(links[0][3])
    new_links[0].append(links[0][0])
    new_links[0].append(links[0][1])
    new_links[0].append(links[0][2])

    new_links[1].append(links[1][3])
    new_links[1].append(links[1][0])
    new_links[1].append(links[1][1])
    new_links[1].append(links[1][2])

    tile[2] = new_links
    return tile

def flipY(tile):
    # print("flip: " + str(tile))
    # for line in tile[1]:
    #     for c in line:
    #         print(c, end='')
    #     print()
    grid = tile[1]
    new_grid = []
    for line in reversed(grid):
        new_grid.append(line)
    tile[1] = new_grid

    links = tile[2]
    new_links = [[] for n in range(2)]
    new_links[0].append(links[0][2][::-1])
    new_links[0].append(links[0][1][::-1])
    new_links[0].append(links[0][0][::-1])
    new_links[0].append(links[0][3][::-1])

    new_links[1].append(links[1][2])
    new_links[1].append(links[1][1])
    new_links[1].append(links[1][0])
    new_links[1].append(links[1][3])
    tile[2] = new_links
    print("flippedy: " + str(tile))
    # for line in tile[1]:
    #     for c in line:
    #         print(c, end='')
    #     print()
    return tile


def flipX(tile):
    # print("flip: ")
    # for line in tile[1]:
    #     for c in line:
    #         print(c, end='')
    #     print()
    grid = tile[1]
    new_grid = []
    for line in grid:
        new_grid.append(line[::-1])
    tile[1] = new_grid

    links = tile[2]
    new_links = [[] for n in range(2)]
    new_links[0].append(links[0][0][::-1])
    new_links[0].append(links[0][3][::-1])
    new_links[0].append(links[0][2][::-1])
    new_links[0].append(links[0][1][::-1])

    new_links[1].append(links[1][0])
    new_links[1].append(links[1][3])
    new_links[1].append(links[1][2])
    new_links[1].append(links[1][1])
    tile[2] = new_links
    print("flippedx: ")
    # for line in tile[1]:
    #     for c in line:
    #         print(c, end='')
    #     print()
    return tile


def load(filename):
    tiles = []
    tile = []
    image = []
    tile_number = 0
    with open(filename) as file:
        for line in file:
            dataline = line.strip("\n")
            if dataline == '':
                tile.append(tile_number)
                tile.append(image)
                tile.append(borders(image))
                tiles.append(tile)
                tile = []
                image = []
            elif dataline.startswith('Tile'):
                tile_number = dataline.strip("Tile ").strip(':')
            else:
                line = []
                for n in dataline:
                    line.append(n)
                image.append(line)

    return tiles


data = load("day20.txt")

for tile in data:
    # print(tile[0])
    for match in data:
        if not tile == match:
            for x in range(4):
                if tile[2][0][x] in match[2][0] or tile[2][0][x][::-1] in match[2][0]:
                    # print(match)
                    tile[2][1][x] = match[0]

prod = 1
for tile in data:
    count = 0
    for match in tile[2][1]:
        if match == '':
            count += 1
    if count == 2:
        prod *= int(tile[0])
        print(tile)
        # if tile[0] == '1951':
        #     corner = flipY(tile)
        corner = tile
print('Answer part 1: ' + str(prod))

final_grid = []

print("starting corner: " + str(corner))
print()
for line in corner[1]:
    for c in line:
        print(c, end='')
    print()

tc = corner[2][1][0]
lc = corner[2][1][3]
print(str(tc) + " " + str(lc))
while (tc != '' or lc != ''):
    corner = rotate(corner)
    tc = corner[2][1][0]
    lc = corner[2][1][3]

print()
print("Rotated corner: " + str(corner))
# print()
# for line in corner[1]:
#     for c in line:
#         print(c, end='')
#     print()

current_tile = corner
vert_pos = 0
for y in range(12):
    print("row start: " + str(current_tile))
    for z in range(len(current_tile[1])):
        if 0 < z < len(current_tile[1]) - 1:
            final_grid.append(current_tile[1][z][1:-1])
    line_tile = current_tile.copy()
    for x in range(11):
        for match in data:
            if line_tile[2][1][1] == match[0]:
                print(match)
                next_tile = match
                while next_tile[2][1][3] != line_tile[0]:
                    #print("rotate..." + str(next_tile[0]))
                    next_tile = rotate(next_tile)

        if next_tile[2][0][3] == line_tile[2][0][1]:
            next_tile = flipY(next_tile)
        print("collumn continue: " + str(x) + str(y) +"  " + str(next_tile))
        for xx in range(len(next_tile[1])):
            r = len(next_tile[1]) - 2
            if 0 < xx < len(next_tile[1]) - 1:
                final_grid[y*r+xx-1] = final_grid[y*r+xx-1] + next_tile[1][xx][1:-1]
        line_tile = next_tile
    #print(str(current_tile))
    for match2 in data:
        #print(str(current_tile[2][1][2]) + " 00000000 " + str(match2))
        if current_tile[2][1][2] == match2[0]:
            next_tile = match2
            while next_tile[2][1][0] != current_tile[0]:
                #print("rotate..." + str(next_tile[0]))
                next_tile = rotate(next_tile)
    if current_tile[2][0][2] == next_tile[2][0][0]:
        next_tile = flipX(next_tile)
    current_tile = next_tile

grid_envelope = []
grid_envelope.append('Final grid')
grid_envelope.append(final_grid)
grid_envelope.append([['.#....#...', '...###.#..', '...#.##..#', '#.#.#####.'], ['', '2473', '2311', '']])

print(grid_envelope)
print()
print()

for line in grid_envelope[1]:
    for n in line:
        print(n, end='')
    print()


def checkForMonster(grid):
    count = 0
    #print(len(grid))
    for x in range(len(grid[0]) - 18):#20):
        for y in range(len(grid) - 1):

            if grid[y][x + 18] == "#" and \
                grid[y + 1][x] == "#" and \
                grid[y + 1][x + 5] == "#" and \
                grid[y + 1][x + 6] == "#" and \
                grid[y + 1][x + 11] == "#" and \
                grid[y + 1][x + 12] == "#" and \
                grid[y + 1][x + 17] == "#" and \
                grid[y + 1][x + 18] == "#" and \
                grid[y + 1][x + 19] == "#" and \
                grid[y + 2][x+1] == "#" and \
                grid[y + 2][x + 4] == "#" and \
                grid[y + 2][x + 7] == "#" and \
                grid[y + 2][x + 10] == "#" and \
                grid[y + 2][x + 13] == "#" and \
                grid[y + 2][x + 16] == "#":
                grid[y][x + 18] = '0'
                grid[y + 1][x] = '0'
                grid[y + 1][x + 5] = '0'
                grid[y + 1][x + 6] = '0'
                grid[y + 1][x + 11] = '0'
                grid[y + 1][x + 12] = '0'
                grid[y + 1][x + 17] = '0'
                grid[y + 1][x + 18] = '0'
                grid[y + 1][x + 19] = '0'
                grid[y + 2][x + 1] = '0'
                grid[y + 2][x + 4] = '0'
                grid[y + 2][x + 7] = '0'
                grid[y + 2][x + 10] = '0'
                grid[y + 2][x + 13] = '0'
                grid[y + 2][x + 16] = '0'
                
                count += 1

    if count > 0:
        print(str(count) +" Monster(s) found")
    else:
        print("-")
    return grid,count

print()
print()
grid_envelope[1] = checkForMonster(grid_envelope[1])[0]
grid_envelope = rotate(grid_envelope)
grid_envelope[1] = checkForMonster(grid_envelope[1])[0]
grid_envelope = rotate(grid_envelope)
grid_envelope[1] = checkForMonster(grid_envelope[1])[0]
grid_envelope = rotate(grid_envelope)
grid_envelope[1] = checkForMonster(grid_envelope[1])[0]
grid_envelope = rotate(grid_envelope)

grid_envelope = flipX(grid_envelope)
grid_envelope[1] = checkForMonster(grid_envelope[1])[0]      #41 found
grid_envelope = rotate(grid_envelope)
grid_envelope[1] = checkForMonster(grid_envelope[1])[0]
grid_envelope = rotate(grid_envelope)
grid_envelope[1] = checkForMonster(grid_envelope[1])[0]
grid_envelope = rotate(grid_envelope)
grid_envelope[1] = checkForMonster(grid_envelope[1])[0]
grid_envelope = rotate(grid_envelope)

grid_envelope = flipX(grid_envelope)
grid_envelope = flipY(grid_envelope)
grid_envelope[1] = checkForMonster(grid_envelope[1])[0]
grid_envelope = rotate(grid_envelope)
grid_envelope[1] = checkForMonster(grid_envelope[1])[0]
grid_envelope = rotate(grid_envelope)
grid_envelope[1] = checkForMonster(grid_envelope[1])[0]    #41 found
grid_envelope = rotate(grid_envelope)
grid_envelope[1] = checkForMonster(grid_envelope[1])[0]
grid_envelope = rotate(grid_envelope)

grid_envelope = flipX(grid_envelope)
grid_envelope[1] = checkForMonster(grid_envelope[1])[0]
grid_envelope = rotate(grid_envelope)
grid_envelope[1] = checkForMonster(grid_envelope[1])[0]
grid_envelope = rotate(grid_envelope)
grid_envelope[1] = checkForMonster(grid_envelope[1])[0]
grid_envelope = rotate(grid_envelope)
grid_envelope[1] = checkForMonster(grid_envelope[1])[0]
grid_envelope = rotate(grid_envelope)

grid_envelope = flipY(grid_envelope)
grid_envelope[1] = checkForMonster(grid_envelope[1])[0]
grid_envelope = rotate(grid_envelope)
grid_envelope[1] = checkForMonster(grid_envelope[1])[0]
grid_envelope = rotate(grid_envelope)
grid_envelope[1] = checkForMonster(grid_envelope[1])[0]    #41 found
grid_envelope = rotate(grid_envelope)
grid_envelope[1] = checkForMonster(grid_envelope[1])[0]
grid_envelope = rotate(grid_envelope)

print()
print()
print()
print()
count = 0
totlcount = 0
monster_count = 0
empty_count = 0
for line in grid_envelope[1]:
    for n in line:
        totlcount += 1
        if n == '#':
            count += 1
            print(',', end='')
        elif n == '0':
            monster_count += 1
            print(n, end='')
        else:
            empty_count += 1
            print(n, end='')
    print()
print("Answer part 2: " +str(count))
print(totlcount)
print(monster_count)
print(empty_count)






