def load(filename):
    data = []
    with open(filename) as file:
        for x, line in enumerate(file):
            dataline = line.strip('\n')
            data.append(int(dataline))
    return data


data = load("Day10/day10.txt")
data.sort()
print(data)

previous = 0
onecount = 0
threecount = 0
for n in data:
    if n - previous == 1:
        onecount += 1
    else:
        threecount += 1
    previous = n
threecount += 1
print(str(onecount) + " " + str(threecount))
print(onecount * threecount)
