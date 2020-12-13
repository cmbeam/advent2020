def load(filename):
    data = []
    with open(filename) as file:
        for y, line in enumerate(file):
            if y == 0:
                timestamp = line.strip('\n')
            else:
                line2 = line.strip('\n')
                times = line2.split(",")
        data.append(timestamp)
        data.append(times)
    return data


def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1

    return lcm


data = load("day13test.txt")
print(data)

# Part 1
lowest = 10000000
lowestbus = 0
for n in data[1]:
    # print(n)
    if n != 'x':
        time = 0
        x = 1
        while time < int(data[0]):
            time = int(n) * x
            x += 1
        print(time - int(data[0]))
        if time - int(data[0]) < lowest:
            lowest = time - int(data[0])
            lowestbus = int(n)
print(lowestbus * lowest)

print()
print()

# # Part 2 take 3
# x = 1
# y = 0
# #for count, n in enumerate(data[1]):
#
#     # print(n)
#    # if n == 'x':
#     #    x += 1
#      #   y += 1
#     #else:
#         # y = 1
# done = False
# while not done:
#     print(str(y) + " " + str(x))
#     #print(divmod(y, int(n)))
#     for count, n in enumerate(data[1]):
#         if n=='x' or (not y==0 and divmod(y, int(n))[1] == 0):
#             ans = y
#             print("bus: " + n + " time: " + str(y))
#
#             y += 1
#             x = ans
#             done = True
#         else:
#             #print("No mtch")
#             done = False
#     y += x

# # Part 2 take 2
# print()
# print()
#
#
#
# period = 1
# pos = 0
# for n in data[1]:
#     print(n)
#     if n == 'x':
#         period += 1
#     else:
#         x = 1
#         while True:
#             print(str(period) + " " + str(x) + " " + str(pos) + " " + str(n))
#             print(divmod(period * x + pos, int(n)))
#             if divmod(period * x + pos, int(n))[1] == 0:
#                 period = period * x + pos
#                 break
#             x += 1
#     print(period)
#     pos += 1

print()
print()

# Part 2
iterations = 0
x = 1
increment = 1
while x < 100000000000000:
    print('x: ' + str(x))
    met = True
    last = (int(data[1][0]) * x) - 1
    for n in data[1]:
        # print(n + "    " + str(last))
        if n == 'x':
            # print('gap')
            last = last + 1
        else:
            #print(str(last) + " " + str(int(n) * x))
            multiplier = last // int(n)
            #print(multiplier)
            time = (multiplier * int(n)) + int(n)
            print(str(last + 1) + " : " + str(time))
            if time == last + 1:
                print("match: " + str(int(n) * x))
                last = time
                increment = last
            else:
                print("No Match  " + str(x) + " match " + str(n))
                met = False
                break
    if met:
        print("Done: " + str(last - len(data[1]) + 1) + "  Iterations: " + str(iterations))
        print("Last: " + str(int(last / int(data[1][len(data[1])-1]))))
        break
    x += 1
    iterations += 1
