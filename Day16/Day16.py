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
errorrate= 0
for ticket in data[2]:
    ticketvalid = True
    for number in ticket:
        numbervalid = False
        for rule in rules:
            for range in rules[rule]:
                if int(range[0]) <= int(number) and int(number) <= int(range[1]):
                    #print("Valid   "+ number + "  " + range[0] + " " + range[1])
                    numbervalid = True
        if not numbervalid:
            ticketvalid = False
            print("INVALID")
            errorrate += int(number)
    if not ticketvalid:
        print("remove ticket " + str(ticket))

print(errorrate)
