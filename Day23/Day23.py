limit = 1000000


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class CreateList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head
        self.nodelist = {}

    def add(self, data):
        new_node = Node(data)
        if self.head.data is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
        self.nodelist[data] = new_node

    def remove(self):
        current = self.head
        removed_nodes = []
        for n in range(3):
            removed_nodes.append(current.next.data)
            self.nodelist.pop(current.next.data)
            current.next = current.next.next
        return removed_nodes

    def insert(self, data):
        current = self.head
        value = current.data
        target = value - 1
        if target == 0:
            target = limit
        while target in data:
            target -= 1
            if target == 0:
                target = limit

        current = self.nodelist[target]

        new_node = Node(data[2], current.next)
        self.nodelist[data[2]] = new_node

        newNode2 = Node(data[1], new_node)
        self.nodelist[data[1]] = newNode2

        newNode3 = Node(data[0], newNode2)
        self.nodelist[data[0]] = newNode3

        current.next = newNode3

    def move_current(self):
        self.head = self.head.next

    def move_current_to(self, data):
        current = self.nodelist[data]
        self.head = current

    def display(self):
        the_string = ''
        current = self.head
        if self.head is None:
            print("[]")
            return
        else:
            the_string += str(current.data)
            while current.next != self.head:
                current = current.next
                the_string += " " + str(current.data)
        print(the_string)

# cl = CreateList()
# cl.add(1)
# cl.add(3)
# cl.add(2)
# cl.add(2)
# cl.add(2)
# cl.add(9)
# cl.move_current()
# cl.display()
# cl.move_current()
# cl.display()
# cl.display()
# d = cl.remove()
# print(d)
# cl.display()
# cl.move_current()
# cl.display()
# cl.add(d)
# cl.display()
# cl.insert([5,6,7])
# cl.display()


def remove_three(circle, current_value):
    removed = []
    current = circle.index(current_value)
    if len(circle) - current > 3:
        removed.append(circle.pop(current + 1))
        removed.append(circle.pop(current + 1))
        removed.append(circle.pop(current + 1))
    elif len(circle) - current > 2:
        removed.append(circle.pop(current + 1))
        removed.append(circle.pop(current + 1))
        removed.append(circle.pop(0))
    elif len(circle) - current > 1:
        removed.append(circle.pop(current + 1))
        removed.append(circle.pop(0))
        removed.append(circle.pop(0))
    else:
        removed.append(circle.pop(0))
        removed.append(circle.pop(0))
        removed.append(circle.pop(0))

    return removed


def get_destination_cup(circle, current):
    value = current

    for x in range(value-1, 0, -1):
        if x in circle:
            return circle.index(x)
    highest = 0
    for n in circle:
        if n != value and n > highest:
            highest = n
    return circle.index(highest)


def insert_cups(circle, inserts, destination):
    circle.insert(destination+1, inserts[0])
    circle.insert(destination + 2, inserts[1])
    circle.insert(destination + 3, inserts[2])

iter = 10000000

data = [9, 4, 2, 3, 8, 7, 6, 1, 5]

print(data)
val = data[0]

for i in range(100):

    r = remove_three(data, val)
    d = get_destination_cup(data, val)

    insert_cups(data, r, d)

    current_pos = data.index(val)
    if current_pos + 1 < len(data):
        current_pos += 1
    else:
        current_pos = 0
    val = data[current_pos]

print(data)
final_string = ''
starting_index = data.index(1) + 1
while starting_index < len(data):
    final_string += str(data[starting_index])
    starting_index += 1
starting_index = 0
while starting_index < data.index(1):
    final_string += str(data[starting_index])
    starting_index += 1

print("Answer part 1: " + final_string)


#data = [9, 4, 2, 3, 8, 7, 6, 1, 5]

data_ll=CreateList()
data_ll.add(9)
data_ll.add(4)
data_ll.add(2)
data_ll.add(3)
data_ll.add(8)
data_ll.add(7)
data_ll.add(6)
data_ll.add(1)
data_ll.add(5)

for x in range(10, limit+1, 1):
     data_ll.add(x)

for i in range(iter):

    d2 = data_ll.remove()
    #data_ll.display()
    data_ll.insert(d2)
    #data_ll.display()
    data_ll.move_current()


print()
print()
print()



data_ll.move_current_to(1)
answer_set = data_ll.remove()

print("Answer part 2: " + str(answer_set[0] * answer_set[1] ))
