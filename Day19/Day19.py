import regex

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


data = load("day19.txt")

validMessages = getValidFromRule(data[0], '0')
print(validMessages)

count = 0
for message in data[1]:
    #print(message)
    if message in validMessages:
        #print("valid")
        count += 1
print("Answer part 1: " + str(count))
print()
print()


# part 2
fourty_two = validMessages = getValidFromRule(data[0], '42')
thirty_one = validMessages = getValidFromRule(data[0], '31')

print(fourty_two)
reg42 = "("
for exp42 in fourty_two[:-1]:
    reg42 = reg42 + exp42 + '|'
reg42 = reg42 + fourty_two[-1]
reg42 = reg42 + ')'
print(reg42)

print(thirty_one)
reg31 = "("
for exp31 in thirty_one[:-1]:
    reg31 = reg31 + exp31 + '|'
reg31 = reg31 + thirty_one[-1]
reg31 = reg31 + ')'
print(reg31)

print("^("+reg42+"+)(("+reg42+"(?>z|(?1))*"+reg31+"))$")
count = 0
for message in data[1]:
    if regex.match("^"+reg42+"+("+reg42+"(?>z|(?2))*"+reg31+")$", message):
        print(message)
        count+=1
print("Answer part 2: " + str(count))



