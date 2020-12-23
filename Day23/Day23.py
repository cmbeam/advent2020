
def remove_three(circle, current_value):
    removed = []
    current = circle.index(current_value)
    if len(circle) - current > 3:
        removed.append(circle.pop(current + 1))
        removed.append(circle.pop(current + 1))
        removed.append(circle.pop(current + 1))
    elif len(circle) - current > 2:
        removed.append(circle.pop(current + 1))
        removed.append(circle.pop(current + 1))
        removed.append(circle.pop(0))
    elif len(circle) - current > 1:
        removed.append(circle.pop(current + 1))
        removed.append(circle.pop(0))
        removed.append(circle.pop(0))
    else:
        removed.append(circle.pop(0))
        removed.append(circle.pop(0))
        removed.append(circle.pop(0))

    return removed

def get_destination_cup(circle, current):
    value = current


    for x in range(value-1, 0, -1):
        if x in circle:
            return circle.index(x)
    highest = 0
    for n in circle:
        if n != value and n > highest:
            highest = n
    return circle.index(highest)

def insert_cups(circle, inserts, destination):
    circle.insert(destination+1, inserts[0])
    circle.insert(destination + 2, inserts[1])
    circle.insert(destination + 3, inserts[2])



#data = [3, 8, 9, 1, 2, 5, 4, 6, 7]
data = [9, 4, 2, 3, 8, 7, 6, 1, 5]



print(data)
val = data[0]

for i in range(100):
    print('Iteration: ' + str(i))

   # print()
    #print(val)
    #print(data)
    r = remove_three(data, val)
    #print(r)
    #print(data)

    d = get_destination_cup(data, val)
    #print(d)

    insert_cups(data, r, d)
    #print(data)

    current_pos = data.index(val)
    if current_pos + 1 < len(data):
        current_pos += 1
    else:
        current_pos = 0
    val = data[current_pos]

print(data)
final_string = ''
starting_index = data.index(1) + 1
while starting_index < len(data):
    final_string += str(data[starting_index])
    starting_index += 1
starting_index = 0
while starting_index < data.index(1):
    final_string += str(data[starting_index])
    starting_index += 1

print("Answer part 1: " + final_string)


data = [9, 4, 2, 3, 8, 7, 6, 1, 5]

for x in range(10,100,1):
    data.append(x)
# for x in range(10,1000000,1):
#     data.append(x)

circle_combos = []
val = data[0]
add_values_count = 10
# circle_combos.append(data.copy())
for i in range(100000):
    #print('Iteration: ' + str(i))
    # if data in circle_combos:
    #     print("Iterations before repeat: " + str(i))
    #     break
    # else:
    #     circle_combos.append(data.copy())

    # print()
    # print(val)
    # print(data)
    r = remove_three(data, val)
    # print(r)
    # print(data)

    d = get_destination_cup(data, val)
    # print(d)

    insert_cups(data, r, d)
    #print(data)

    current_pos = data.index(val)
    if current_pos + 1 < len(data):
        current_pos += 1
    else:
        current_pos = 0
    val = data[current_pos]

    # insert_point = data.index(1000000)
    # data.insert(insert_point, add_values_count)
    # data.insert(insert_point, add_values_count + 1)
    # data.insert(insert_point, add_values_count + 2)
    # add_values_count += 3
    #
    # # print()
    # # print(val)
    # # print(data)
    # r = remove_three(data, val)
    # # print(r)
    # # print(data)
    #
    # d = get_destination_cup(data, val)
    # # print(d)
    #
    #
    # # current2 = data.index(val)
    # # print("Index: " + str(current2))
    # # if current2 > 3:
    # #     data.insert(data.index(1000000), current2 + 6)
    #     # if d + 2 == len(data):
    #     #     d += 1
    # # print(data)
    # insert_cups(data, r, d)
    #
    # # print(data)
    #
    # current_pos = data.index(val)
    # if current_pos + 1 < len(data):
    #     current_pos += 1
    # else:
    #     current_pos = 0
    # val = data[current_pos]
print(i)
print(data)

print()
print()
print()

data.append(data[0])
data.append(data[1])
starting_index = data.index(1) + 1
print(data[starting_index])
print(data[starting_index+1])
print("Answer part 2: " + str(data[starting_index] * data[starting_index+1]))
