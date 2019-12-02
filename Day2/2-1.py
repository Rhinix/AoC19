problemInput = [int(i) for i in (open("input2-1.txt").read().split(","))]

problemInput[1] = 12
problemInput[2] = 2

# print(problemInput)

for i in range(0, len(problemInput), 4):
    if problemInput[i] == 1:
        problemInput[problemInput[i+3]] = problemInput[problemInput[i+1]] + \
            problemInput[problemInput[i+2]]
    elif problemInput[i] == 2:
        problemInput[problemInput[i+3]] = problemInput[problemInput[i+1]] * \
            problemInput[problemInput[i+2]]
    elif problemInput[i] == 99:
        break

print(problemInput[0])
