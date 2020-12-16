def load(filename):
    rules = {}
    myticket = []
    tickets = []
    file = open(filename)
    line = file.readline().strip('\n')
    while not line == "your ticket:":
        name = line.split(": ")[0]
        ranges = [line.split(": ")[1].split(" or ")[0].split('-'), line.split(": ")[1].split(" or ")[1].split('-')]
        rules[name] = ranges
        line = file.readline().strip('\n')
    line = file.readline().strip('\n')
    myticket = line.split(',')
    file.readline()
    for line in file:
        tickets.append(line.strip('\n').split(','))

    file.close()
    return rules, myticket,tickets


data = load("day16.txt")
rules = data[0]
tickets = data[2]
newticketlist = tickets.copy()
errorrate= 0
for ticket in tickets:
    ticketvalid = True
    for number in ticket:
        numbervalid = False
        for rule in rules:
            for rangerule in rules[rule]:
                if int(rangerule[0]) <= int(number) and int(number) <= int(rangerule[1]):
                    numbervalid = True
        if not numbervalid:
            ticketvalid = False
            errorrate += int(number)
    if not ticketvalid:
        newticketlist.remove(ticket)

print("Answer part 1: " + str(errorrate))

newticketlist.append(data[1])

# Part 2
mapping = {}
for rule in rules:
    mapping[rule] = []
    nameValid = True
    for x in range(len(newticketlist[0])):
        for ticket in newticketlist:
            inrange = False
            for rangerule in rules[rule]:
                if int(rangerule[0]) <= int(ticket[x]) and int(ticket[x]) <= int(rangerule[1]):
                    inrange = True
            if not inrange:
                namevalid = False
        if namevalid:
            mapping[rule] = mapping[rule] + [x]

        namevalid = True


def removeRowMapping(mapping, row):
    for name in mapping:
        if len(mapping[name]) != 1 and row in mapping[name]:
            mapping[name].remove(row)
    return mapping


done = False
while not done:
    done = True
    for rule in mapping:
        if len(mapping[rule]) == 1:
            mapping = removeRowMapping(mapping, mapping[rule][0])
        else:
            done = False

print("Mapping:   " + str(mapping))

product = 1
for name in mapping:
    if name.startswith('departure'):
        product *= int(data[1][mapping[name][0]])
print("Answer part 2: " + str(product))


