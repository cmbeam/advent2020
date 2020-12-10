import itertools


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
onelist = []
threelist = []
for n in data:
    if n - previous == 1:
        onecount += 1
        onelist.append(n)
    else:
        threecount += 1
        threelist.append(previous)
        if onelist.__contains__(previous):
            onelist.remove(previous)
        threelist.append(n)

    previous = n
threecount += 1
print(str(onecount) + " " + str(threecount))
print(onecount * threecount)

# Part 2
print(onelist)
print(threelist)

combocount = 1
groupthreecount = 0
for y, n in enumerate(data):
    if n not in threelist:
        groupthreecount += 1
    else:
        print("span count: " + str(groupthreecount))
        if groupthreecount == 3:
            combocount *= 7
        if groupthreecount == 2:
            combocount *= 4
        if groupthreecount == 1:
            combocount *= 2

        groupthreecount = 0
print("answer: " + str(combocount))





#perm = itertools.permutations(data)
#for i in list(perm):
#    print(i)
