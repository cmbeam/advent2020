def load(filename):
    data = {}
    z = 0
    y = 0 - int(len(open(filename).readlines()) / 2)
    with open(filename) as file:
        for line in file:
            dataline = line.strip("\n")
            x = 0 - (int((len(dataline) / 2)))
            for cube in dataline:
                if cube == '#':
                    data[x, y, z] = 1
                else:
                    data[x, y, z] = 0
                x += 1
            y += 1

    return data

def create_cube(cubes, coord):
    expanded_cubes = cubes.copy()
    if not coord in cubes:
        expanded_cubes[coord] = 0
    return expanded_cubes



data = load('day17.txt')

cubes = data
z_depth = 1
turns = 6
print(cubes)

for i in range(turns):

    # Expand cubes
    for cube in cubes:
        #print(str(cube) + " " + str(cubes[cube]))
        for z in range(cube[2] - 1, cube[2] + 2):
            for y in range(cube[1] - 1, cube[1] + 2):
                for x in range(cube[0] - 1, cube[0] + 2 ):
                    cubes = create_cube(cubes, (x, y, z))
    # Process cube state
    temp_cubes = cubes.copy()
    for cube in cubes:
        count = 0
        for z in range(cube[2] - 1, cube[2] + 2):
            for y in range(cube[1] - 1, cube[1] + 2):
                for x in range(cube[0] - 1, cube[0] + 2 ):
                    if (x, y, z) in cubes and cubes[x, y, z] == 1:
                        count += 1
        #print(count)
        if cubes[cube] == 1:
            count -= 1
            if count == 2 or count == 3:
                temp_cubes[cube] = 1
            else:
                temp_cubes[cube] = 0
        else:
            if count == 3:
                temp_cubes[cube] = 1
            else:
                temp_cubes[cube] = 0
    cubes = temp_cubes
    print(cubes)
    print("Number: " + str(len(cubes)))
    round_count = 0
    for cube in cubes:
        if cubes[cube] == 1:
            round_count += 1
    print("Round count: "+ str(round_count))


final_count = 0
for cube in cubes:
    if cubes[cube] == 1:
        final_count += 1
print(final_count)







#data  = load('day17.txt')
#print(data)

