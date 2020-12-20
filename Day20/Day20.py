def borders(grid):
    borders=['' for n in range(4)]
    border_strings = []
    links = []
    borders[0] = grid[0][0:]
    for line in grid:
        borders[1] = borders[1] + line[len(line) - 1]
    for line in reversed(grid):
        borders[3] = borders[3] + line[0]
    borders[2] = grid[-1][::-1]
    for border in borders:
        border_string =""
        for n in border:
            border_string = border_string + n
            link = '0'
        border_strings.append(border_string)
        links.append('')

    return border_strings, links

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
    print(tile[0])
    for match in data:
        if not tile == match:
            for x in range(4):
                if tile[2][0][x] in match[2][0] or tile[2][0][x][::-1] in match[2][0]:
                    print(match)
                    tile[2][1][x] = match[0]
            else:
                print(tile[2][0][0]+ "  " + match[2][0][0])

prod = 1
for tile in data:
    count = 0
    for match in tile[2][1]:
        if match =='':
            count += 1
    if count == 2:
        print("Corner: " + tile[0])
        prod *= int(tile[0])
    print(tile)
print('Answer part 1: '+ str(prod))