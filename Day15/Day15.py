import array as myarray

def load(filename):
    data = []
    with open(filename) as file:
        for line in file:
            dataline = line.strip("\n")
            data = dataline.split(',')
    return data


data = load("day15.txt")
print("Seed data: " + str(data))
# originalData = data.copy()
#
# turns = 2020
#
# for x in range(turns):
#     if x == len(data):
#         previous = data[x - 1]
#         if previous in data[:x-1]:
#             lastIndex =  data[x-2::-1].index(previous)
#             age = lastIndex + 1
#             data.append(str(age))
#         else:
#             data.append('0')
#
# print("Final list part 1: " + str(data))
# print("Answer part 1: " + data[turns - 1])
#
#
#
# # Part 2
# data = originalData.copy()

turns = 30000000

previous = 0

lastPositions = [-1 for x in range(turns)]
for x, num in enumerate(data):
    lastPositions[int(num)] = x
    previous = int(num)
print("setup complete")
length = len(data)
x = 0
while x < turns:
    if x >= length:
        lastPosition = lastPositions[previous]
        if lastPosition != -1 and lastPosition != x - 1:
            age = x - lastPosition - 1
            lastPositions[previous] = x - 1
            previous = age
        else:
            lastPositions[previous] = x - 1
            previous = 0
    x += 1
print("Answer part 2: " + str(previous))

