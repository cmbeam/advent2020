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
            print(seatid)
            seats[seatid] = 1
            if seatid > highest:
                highest = seatid
    y = 0
    for x in seats:
        if x == 0 and seats[y-1] == 1 and seats[y+1] == 1:
            print("My seat: "+ str(y))
        y = y + 1
    return highest


# Load file
file = 'Day5/day5.txt'

# Part 1
answer = loadpuzzle(file)
print("highest seat id: " + str(answer))
