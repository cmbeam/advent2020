

def getparents(tree, child, runninglist):
    # print(runninglist)
    list_of_keys = [key
                        for key, list_of_values in tree.items()
                        for item in list_of_values
                        if child in item]
    #print(str(child) + " in: " + str(list_of_keys))
    if not list_of_keys:
        # print("done " + str(child))
        return runninglist
    #print(str(list_of_keys))
    for key in list_of_keys:
        runninglist.add(key)
        runninglist = getparents(tree, key, runninglist)

    return runninglist


def getchildren(tree, parent):
    total = 0
    # print(parent)
    list_of_children = tree[parent]
    # print(parent + "::" + str(list_of_children))
    if 'other' in list_of_children:
        return 1
    for child in list_of_children:
        total = total + getchildren(tree, child[0]) * int(child[1])
        # print(str(child) + " " + str(total))
    # print(runningTotal)
    return total + 1



def loadpuzzle(file):
    parents = {}

    x = 0
    with open(file) as puzzle:
        for line in puzzle:
            line = line.strip('.\n')
            parts = line.split(' bags contain ')
            parent = parts[0]
            children = parts[1].split(', ')

            # print(parent)
            # print(children)
            x = x + 1
            for child in children:
                child = child.strip('bags')
                child = child.strip('bag')
                childp = child.split(' ')
                color = [0 for i in range(2)]
                color[0] = childp[1] + " " + childp[2]
                color[1] = childp[0]
                # print("parent: " + parent + "  child: " + color)
                if parent in parents:
                    existing = parents[parent]
                else:
                    existing = []
                if childp[1] == 'other':
                    existing.append(childp[1])
                else:
                    existing.append(color)
                parents[parent] = existing


    return parents


tree = loadpuzzle("Day7/day7.txt")
print(tree)

# Part 1
list = set()
# list.add("shiny gold")
finalList = getparents(tree, "shiny gold", list)
print(len(finalList))

# Part 2
total = 0
print(getchildren(tree, "shiny gold") - 1)

