
class Node:
  def __init__(self,data, next_node=None):
    self.data = data;
    self.next = next_node;

class CreateList:
  #Declaring head and tail pointer as null.
    def __init__(self):
        self.head = Node(None);
        self.tail = Node(None);
        self.head.next = self.tail;
        self.tail.next = self.head;
    def add(self, data):
        newNode = Node(data);
        # Checks if the list is empty.
        if self.head.data is None:
            # If list is empty, both head and tail would point to new node.
            self.head = newNode;
            self.tail = newNode;
            newNode.next = self.head;
        else:
            # tail will point to new node.
            self.tail.next = newNode;
            # New node will become new tail.
            self.tail = newNode;
            # Since, it is circular linked list tail will point to head.
            self.tail.next = self.head;

    def remove(self):
        current = self.head
        removed_nodes = []
        for n in range(3):
            removed_nodes.append(current.next.data)
            current.next = current.next.next

        return removed_nodes

    def insert(self, data):
        current = self.head
        value = current.data
        print("value: " + str(value))
        highest = 0
        while (current.next != self.head):
            current = current.next
            if current.data > highest:
                highest = current.data
            if current.data < value:
                for d in reversed(data):
                    newNode = Node(d, current.next)
                    current.next = newNode
                break
        print("highest: " + str(highest))
        current = self.head
        while (current.next != self.head):
            current = current.next
            if current.data == highest:
                for d in reversed(data):
                    newNode = Node(d, current.next)
                    current.next = newNode
                break



    def move_current(self):
        self.head = self.head.next

    def display(self):
        current = self.head
        if self.head is None:
          print("List is empty")
          return;
        else:
            print("Nodes of the circular linked list: ")
            #Prints each node by incrementing pointer.
            print(current.data),
            while(current.next != self.head):
                current = current.next
                print(current.data),

cl = CreateList()
cl.add(1)
cl.add(3)
cl.add(2)
cl.add(2)
cl.add(2)
cl.add(9)
cl.move_current()
cl.display()
cl.move_current()
cl.display()
cl.display()
d = cl.remove()
print(d)
cl.display()
cl.move_current()
cl.display()
cl.add(d)
cl.display()
cl.insert([5,6,7])
cl.display()

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



#data = [3, 8, 9, 1, 2, 5, 4, 6, 7]
data = [9, 4, 2, 3, 8, 7, 6, 1, 5]



print(data)
val = data[0]

for i in range(100):
    print('Iteration: ' + str(i))

   # print()
    #print(val)
    #print(data)
    r = remove_three(data, val)
    #print(r)
    #print(data)

    d = get_destination_cup(data, val)
    #print(d)

    insert_cups(data, r, d)
    #print(data)

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


data = [9, 4, 2, 3, 8, 7, 6, 1, 5]

for x in range(10,100,1):
    data.append(x)
# for x in range(10,1000000,1):
#     data.append(x)

circle_combos = []
val = data[0]
add_values_count = 10
# circle_combos.append(data.copy())
for i in range(100000):
    #print('Iteration: ' + str(i))
    # if data in circle_combos:
    #     print("Iterations before repeat: " + str(i))
    #     break
    # else:
    #     circle_combos.append(data.copy())

    # print()
    # print(val)
    # print(data)
    r = remove_three(data, val)
    # print(r)
    # print(data)

    d = get_destination_cup(data, val)
    # print(d)

    insert_cups(data, r, d)
    #print(data)

    current_pos = data.index(val)
    if current_pos + 1 < len(data):
        current_pos += 1
    else:
        current_pos = 0
    val = data[current_pos]

    # insert_point = data.index(1000000)
    # data.insert(insert_point, add_values_count)
    # data.insert(insert_point, add_values_count + 1)
    # data.insert(insert_point, add_values_count + 2)
    # add_values_count += 3
    #
    # # print()
    # # print(val)
    # # print(data)
    # r = remove_three(data, val)
    # # print(r)
    # # print(data)
    #
    # d = get_destination_cup(data, val)
    # # print(d)
    #
    #
    # # current2 = data.index(val)
    # # print("Index: " + str(current2))
    # # if current2 > 3:
    # #     data.insert(data.index(1000000), current2 + 6)
    #     # if d + 2 == len(data):
    #     #     d += 1
    # # print(data)
    # insert_cups(data, r, d)
    #
    # # print(data)
    #
    # current_pos = data.index(val)
    # if current_pos + 1 < len(data):
    #     current_pos += 1
    # else:
    #     current_pos = 0
    # val = data[current_pos]
print(i)
print(data)

print()
print()
print()

data.append(data[0])
data.append(data[1])
starting_index = data.index(1) + 1
print(data[starting_index])
print(data[starting_index+1])
print("Answer part 2: " + str(data[starting_index] * data[starting_index+1]))
