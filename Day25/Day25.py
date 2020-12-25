def load(filename):
    data = []
    with open(filename) as file:
        for line in file:
            data_line = line.strip("\n")
            data.append(data_line)
    return data


def get_loop_size(public_key):
    subject_number = 7
    calculated_key = 1
    loop = 0
    while calculated_key != int(public_key):
        calculated_key *= subject_number
        calculated_key = divmod(calculated_key, 20201227)[1]
        loop += 1
    return loop


def get_encryption_key(public_key, loop_size):
    calculated_key = 1
    subject_number = public_key
    for n in range(loop_size):
        calculated_key *= subject_number
        calculated_key = divmod(calculated_key, 20201227)[1]
    return calculated_key


data = load('day25.txt')

card_public = data[0]
door_public = data[1]

card_loop = get_loop_size(card_public)
door_loop = get_loop_size(door_public)

print(card_loop)
print(door_loop)
encryption_key = get_encryption_key(int(door_public), card_loop)
print(encryption_key)
encryption_key = get_encryption_key(int(card_public), door_loop)
print(encryption_key)
print()
print("Answer part 1: " + str(encryption_key))



