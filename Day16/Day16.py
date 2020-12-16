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
        line = line.strip('\n')
        tickets.append(line.split(','))

    file.close()
    return rules, myticket,tickets


data = load("day16.txt")
print(data[0])
print(data[1])
rules = data[0]
tickets = data[2]

errorrate= 0
for ticket in tickets:
    ticketvalid = True
    for number in ticket:
        numbervalid = False
        for rule in rules:
            for range in rules[rule]:
                if int(range[0]) <= int(number) and int(number) <= int(range[1]):
                    numbervalid = True
        if not numbervalid:
            ticketvalid = False
            errorrate += int(number)
    if not ticketvalid:
        print("remove ticket " + str(ticket))
        tickets.remove(ticket)

print("Answer part1: " + str(errorrate))

# Part 2

