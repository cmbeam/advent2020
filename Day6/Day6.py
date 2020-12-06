# Load file
def loadpuzzle(file):
    resultJoin = {}
    resultInt = {}
    answers = set()
    answer = {}
    x = 0
    y = 0
    with open(file) as puzzle:
        for line in puzzle:
            line = line.strip('\n')
            if line == '':
                resultJoin[y] = answers
                result = answer[0]
                for i in answer:
                    result = result.intersection(answer[i])
                resultInt[y] = result
                answers = set()
                answer = {}
                x = 0
                y = y + 1
            else:
                answer[x] = set()
                for n in line:
                    answers.add(n)
                    answer[x].add(n)
                x = x + 1

    return resultJoin, resultInt


resultSet1, resultSet2 = loadpuzzle("Day6/day6.txt")

# Part 1
count = 0
for x in resultSet1:
    count = count + len(resultSet1[x])
print("Part1: " + str(count))

# Part 2
count = 0
for x in resultSet2:
    count = count + len(resultSet2[x])
print("Part2: " + str(count))
