

def getparents(tree, child, runninglist):
    # runninglist.add(child)
    print(runninglist)
    list_of_keys = [key
                        for key, list_of_values in tree.items()
                        if child in list_of_values]
    # print(str(child) + " in: " + str(list_of_keys))
    if not list_of_keys:
        # print("done " + str(child))
        return runninglist
    #print(str(list_of_keys))
    for key in list_of_keys:
        runninglist.add(key)
        runninglist = getparents(tree, key, runninglist)

    return runninglist


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
                color = childp[1] + " " + childp[2]
                # print("parent: " + parent + "  child: " + color)
                if parent in parents:
                    existing = parents[parent]
                else:
                    existing = []
                existing.append(color)
                parents[parent] = existing


    return parents


tree = loadpuzzle("Day7/day7.txt")
#print(tree)
list = set()
#list.add("shiny gold")
finalList = getparents(tree, "shiny gold", list)
print(len(finalList))

