def load(filename):
    rules = {}
    messages = []
    file = open(filename)
    line = file.readline().strip('\n')
    while not line == "":
        name = line.split(": ")[0]
        rule = [line.split(": ")[1].split(" | ")]
        rules[name] = rule
        line = file.readline().strip('\n')
    #line = file.readline().strip('\n')
    for line in file:
        messages.append(line.strip('\n'))

    file.close()
    return rules, messages

data = load("day19.txt")
#print(data[0])
#print(data[1])


def getValidFromRule(rules, rule_number):
    validMessages = []
    #print(str(rule_number) + str(rules[rule_number][0]))
    rule = rules[rule_number][0]
    if str(rule[0]).startswith('"'):
        validMessages.append(rule[0].strip('"'))
    else:
        for rule in rules[rule_number][0]:
            combos = ['']
            for spot in rule.split(' '):
                mess = getValidFromRule(rules, spot)
                meslist = []
                for mes in mess:
                    meslist.append(mes)
                nCombos = []
                for messi in meslist:
                    #print(combos)
                    for combo in combos:
                        #print("Combo " + combo)
                        nCombos.append(combo + messi)
                combos = nCombos
                #print(str(rule_number) +" intra: " + str(combos))
            #print(combos)
            validMessages = validMessages + combos







    #print("messages: " + str(validMessages))
    return validMessages

validMessages = getValidFromRule(data[0], '0')
#print(validMessages)

count = 0
for message in data[1]:
    #print(message)
    if message in validMessages:
        #print("valid")
        count += 1
print("Answer part 1: " + str(count))


# part 2

