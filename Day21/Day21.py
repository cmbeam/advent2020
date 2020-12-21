def load(filename):
    data = []
    with open(filename) as file:
        x = 0
        for line in file:
            dataline = line.strip("\n")
            parts = dataline.split(' (contains ')
            ingriedients = parts[0].split(' ')
            alergens = parts[1].strip(')').split(', ')
            item = []
            item.append(x)
            item.append(ingriedients)
            item.append(alergens)
            data.append(item)
            x += 1
    return data


def intersection(first, *others):
    return set(first).intersection(*others)

data = load("day21.txt")
print(data)

allergen_lists = {}
for n in data:
    for allergen in n[2]:
        if not allergen_lists.get(allergen):
            allergen_lists[allergen] = [n[1]]
        else:
            list_a = allergen_lists[allergen]
            list_a.append(n[1])
            allergen_lists[allergen] = list_a

ingredient_mapping = {}
for all_list in allergen_lists:
    print(all_list)
    intersected = set(allergen_lists[all_list][0]).intersection(*allergen_lists[all_list])
    print(intersected)
    ingredient_mapping[all_list] = intersected
    # for inter in intersected:
    #     if not ingredient_mapping.get(inter):
    #         ingredient_mapping[inter] = [all_list]
    #     else:
    #         list_i = ingredient_mapping[inter]
    #         list_i.append(all_list)
    #         ingredient_mapping[inter] = list_i
print()
print(ingredient_mapping)

complete = False
while not complete:
    complete = True
    for n in ingredient_mapping:
        if len(ingredient_mapping[n]) > 1:
            complete = False
        else:
            for m in ingredient_mapping:
                remove_item = ingredient_mapping[n]
                #print(remove_item)

                if m != n:
                    if ingredient_mapping[m].intersection(remove_item):
                        print("REMove " + str(remove_item))
                        cleaned_list = ingredient_mapping[m]
                        print(cleaned_list)
                        cleaned_list = cleaned_list - remove_item
                        print(cleaned_list)
                        ingredient_mapping[m] = cleaned_list

print(ingredient_mapping)