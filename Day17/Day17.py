def load(filename):
    data = {}
    w = 0
    z = 0
    y = 0 - int(len(open(filename).readlines()) / 2)

    with open(filename) as file:
        rows = 15
        for line in file:
            dataline = line.strip("\n")
            x = 0 - (int((len(dataline) / 2)))
            for cube in dataline:
                if cube == '#':
                    data[w, z, y, x] = 1
                else:
                    data[w, z, y, x] = 0
                x += 1
            y += 1
        print(data)
        # Expand cubes
        for w in range(-rows, rows+1):
            for z in range(-rows, rows+1):
                for y in range(-rows, rows+1):
                    for x in range(-rows, rows+1):
                        if not (w,z,y,x) in data:
                            data[w,z,y,x] = 0

    return data

def create_cube(cubes, coord):
    expanded_cubes = cubes.copy()
    if not coord in cubes:
        expanded_cubes[coord] = 0
    return expanded_cubes

def print_cube(cubes):
    sortedcs = sorted(cubes)
    #print(cubes)
    #print(sortedcs)
    w_start = sortedcs[0][0]
    z_start = sortedcs[0][1]
    y_start = sortedcs[0][2]
    print("W: " + str(w_start))
    print("Z: " + str(z_start))
    for cube in sortedcs:
        if cube[0] > w_start:
            w_start += 1
            z_start = sortedcs[0][1] - 1
        if cube[1] > z_start:
            z_start += 1
            y_start = sortedcs[0][2]
            print("\nw: " + str(w_start))
            print("Z: " + str(z_start))
        if cube[2] > y_start:
            y_start += 1
            print("")
        print(cubes[cube], end='')
    print()


data = load('day17.txt')

cubes = data
z_depth = 1
turns = 6
#print_cube(cubes)

for i in range(turns):
    print("Iteration: " + str(i))

    # # Expand cubes
    # for cube in cubes:
    #     #print(str(cube) + " " + str(cubes[cube]))
    #     for w in range(cube[0] - 1, cube[0] + 2):
    #         for z in range(cube[1] - 1, cube[1] + 2):
    #             for y in range(cube[2] - 1, cube[2] + 2):
    #                 for x in range(cube[3] - 1, cube[3] + 2 ):
    #                     cubes = create_cube(cubes, (w, z, y, x))
    # Process cube state
    temp_cubes = cubes.copy()
    for cube in cubes:
        count = 0
        if abs(cube[0]) <= i + 1 and abs(cube[1]) <= i + 1:
            for w in range(cube[0] - 1, cube[0] + 2):
                for z in range(cube[1] - 1, cube[1] + 2):
                    for y in range(cube[2] - 1, cube[2] + 2):
                        for x in range(cube[3] - 1, cube[3] + 2 ):
                            if (w, z, y, x) in cubes and cubes[w, z, y, x] == 1:
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
    #print(sorted(cubes))
    #print_cube(cubes)

    # print("Number: " + str(len(cubes)))
    # round_count = 0
    # for cube in cubes:
    #     if cubes[cube] == 1:
    #         if cube[0] != 0:
    #             round_count += 2
    #         else:
    #             round_count += 1
    # print(str(i+1) + " Round count: "+ str(round_count))


final_count = 0
for cube in cubes:
    if cubes[cube] == 1:
        final_count += 1
print(final_count)







#data  = load('day17.txt')
#print(data)

