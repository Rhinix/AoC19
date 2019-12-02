def main():
    print(getAnswer())


def getAnswer():
    for i in range(0, 100):
        for j in range(0, 100):
            problemInput = [int(i)
                            for i in (open("input2-2.txt").read().split(","))]
            problemInput[1] = i
            problemInput[2] = j
            answer = processOpcode(problemInput)
            if answer[0] == 19690720:
                return 100*answer[1]+answer[2]


def processOpcode(opcode):
    for i in range(0, len(opcode), 4):
        if opcode[i] == 1:
            opcode[opcode[i+3]] = opcode[opcode[i+1]] + \
                opcode[opcode[i+2]]
        elif opcode[i] == 2:
            opcode[opcode[i+3]] = opcode[opcode[i+1]] * \
                opcode[opcode[i+2]]
        elif opcode[i] == 99:
            return opcode
    return opcode


if __name__ == "__main__":
    main()
