def BinaryToDecimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    return decimal

# Load file
def loadpuzzle(file):
    highest = 0
    seats = [0 for j in range(128*8)]
    with open(file) as puzzle:
        for line in puzzle:
            line = line.strip('\n')
            line = line.replace('F', '0')
            line = line.replace('B', '1')
            line = line.replace('L', '0')
            line = line.replace('R', '1')
            row = line[:7]
            column = line[7:]
            rownum = BinaryToDecimal(row)
            columnnum = BinaryToDecimal(column)
            seatid = (rownum * 8) + columnnum
            seats[seatid] = 1
    return seats


# Load file
file = 'Day5/day5.txt'
seats = loadpuzzle(file)

# Part 1
highest = 0
for x, occupied in enumerate(seats):
    if occupied == 1:
        highest = x
print("highest seat id: " + str(highest))

# Part 2
y = 0
for x, occupied in enumerate(seats):
    if occupied == 0 and seats[x - 1] == 1 and seats[x + 1] == 1:
        print("My seat id: " + str(x))
