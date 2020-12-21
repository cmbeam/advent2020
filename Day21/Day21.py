def load(filename):
    data = []
    with open(filename) as file:
        x = 0
        for line in file:
            data_line = line.strip("\n")
            parts = data_line.split(' (contains ')
            ingredients = parts[0].split(' ')
            allergens = parts[1].strip(')').split(', ')
            item = []
            item.append(x)
            item.append(ingredients)
            item.append(allergens)
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
    intersected = set(allergen_lists[all_list][0]).intersection(*allergen_lists[all_list])
    ingredient_mapping[all_list] = intersected


complete = False
while not complete:
    complete = True
    for n in ingredient_mapping:
        if len(ingredient_mapping[n]) > 1:
            complete = False
        else:
            for m in ingredient_mapping:
                remove_item = ingredient_mapping[n]
                if m != n:
                    if ingredient_mapping[m].intersection(remove_item):
                        cleaned_list = ingredient_mapping[m]
                        cleaned_list = cleaned_list - remove_item
                        ingredient_mapping[m] = cleaned_list

print(ingredient_mapping)

count = 0
for item in data:
    list_of_ingredients = item[1]
    for ingredient in list_of_ingredients:
        match = False
        for defined in ingredient_mapping:
            for t in ingredient_mapping[defined]:
                value = t
            if ingredient == value:
                match = True
        if not match:
            count += 1
print("Answer part 1: " + str(count))

print()
print("Answer part 2: ", end='')
answer_part_2 = ''
sorted_keys = sorted(ingredient_mapping.keys())
for key in sorted_keys:
    for value in ingredient_mapping[key]:
        print(value+',', end='')
print()

