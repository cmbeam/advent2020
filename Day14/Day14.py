
def load(filename):
    data = []
    with open(filename) as file:
        for x, line in enumerate(file):
            dataline = line.strip('\n')
            instruction = dataline.split(" = ")
            if not instruction[0] == 'mask':
                instruction[0] = instruction[0].strip('mem[').strip("]")
                binarystring = str(bin(int(instruction[1])))[2:]
                print(binarystring)
                binaryaddzeros = ""
                for i in range(36 - len(binarystring)):
                    binaryaddzeros = binaryaddzeros + '0'
                instruction[1] = binaryaddzeros + binarystring

            data.append(instruction)

    return data


data = load("day14.txt")
print(data)
mask = ['X' for x in range(36)]
mem = [[0 for x in range(36)] for y in range(65484)]


for line in data:
    if line[0] == 'mask':
        for x, n in enumerate(line[1]):
            mask[x] = n
    else:
        print("mask:         ", end='')
        for maskb in mask:
            print(maskb, end='')
        print()
        print("instruction:  " + line[1])

        for y, bit in enumerate(reversed(line[1])):
            maskbit = mask[35-y]
            if maskbit == 'X':
                mem[int(line[0])][35-y] = int(bit)
            else:
                mem[int(line[0])][35-y] = int(maskbit)

        print("written:      ", end='')
        for bit in mem[int(line[0])]:
            print(bit, end='')
        print()

sum = 0
for address in mem:

    decimal = 0
    for digit in address:
        decimal = decimal*2 + int(digit)
    sum += decimal
    if decimal > 0:
        print("memory:  ", end='')
        binary = ''
        for bit in address:
            print(bit, end='')
            binary = binary + str(bit)
        print("   decimal:  " + str(decimal) + "  sum: "+ str(sum) )

print("PArt 1:  " + str(sum))

# Part 2
mem = {}


for line in data:
    if line[0] == 'mask':
        for x, n in enumerate(line[1]):
            mask[x] = n
    else:
        print("mask:         ", end='')
        for maskb in mask:
            print(maskb, end='')
        print()
        print("instruction:  " + line[1])

        addr = str(bin(int(line[0])))[2:]
        print(addr)
        newAddr = ""
        for x in range(36 - len(addr)):
            newAddr = newAddr + '0'
        newAddr = newAddr + addr
        print(newAddr)
        adrresToBeWritten = [0 for x in range(36)]
        for y, bit in enumerate(reversed(newAddr)):
            maskbit = mask[35-y]
            if maskbit == 'X':
                adrresToBeWritten[35 - y] = 'X'
            else:
                if maskbit == '0':
                    if bit:
                        adrresToBeWritten[35 - y] = int(bit)
                    else:
                        adrresToBeWritten[35 - y] = int(bit)
                else:
                    adrresToBeWritten[35 - y] = 1
        print(adrresToBeWritten)
        def updateAddressList(digit, addresses):
            newAddresses = []
            if digit == 'X':
                for address in addresses:
                    #print(address)
                    newAddresses.append('1' + str(address))
                    newAddresses.append('0' + str(address))
            else:
                for address in addresses:
                    #print(address)
                    newAddresses.append(str(digit) + str(address))
            return newAddresses
        addressesToBeWritten = ['']
        for bit in reversed(adrresToBeWritten):
            addressesToBeWritten = updateAddressList(bit, addressesToBeWritten)
            # print(bit, end='')
        print(addressesToBeWritten)
        for address in addressesToBeWritten:
            decimal = 0
            for digit in address:
                decimal = decimal * 2 + int(digit)
            print(decimal)
            decimalLine1 = 0
            for digit in line[1]:
                decimalLine1 = decimalLine1 * 2 + int(digit)
            print(decimalLine1)
            mem[decimal] = decimalLine1
        print()



sum = 0
for address in mem:
    print(address)
    sum += mem[address]
    if decimal > 0:
        print("memory:  " + str(mem[address]), end='')
        print("   decimal:  " + str(decimal) + "  sum: "+ str(sum) )

print("Part 2:  " + str(sum))
