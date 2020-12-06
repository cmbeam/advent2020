# Load file
def loadpuzzle(file):
    highest = 0
    seats = [0 for j in range(128*8)]
    count1 = 0
    count2 = 0
    answers=set()
    answer={}
    x = 0
    with open(file) as puzzle:
        for line in puzzle:
            line = line.strip('\n')
            if line == '':
                print(str(answers) + str(len(answers)))
                count1 = count1 + len(answers)
                result = answer[0]
                for i in answer:
                    print(result)
                    print(answer[i])
                    result = result.intersection(answer[i])
                print(result)
                print(len(result))
                count2 = count2 + len(result)
                answers = set()
                answer = {}
                x = 0
            else:
                answer[x] = set()
                for n in line:
                    answers.add(n)
                    answer[x].add(n)
                x = x + 1;

    return count2


answer = loadpuzzle("Day6/day6.txt")
print(answer)
