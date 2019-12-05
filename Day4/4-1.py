passwordsToTry = [x for x in range(248345, 746315)]


def hasTwoSameAdjacentDigit(password):
    for x in range(0, len(password)-1):
        if password[x] == password[x+1]:
            return True

    return False


def isIncreasing(password):
    for x in range(0, len(password)-1):
        if not(password[x] <= password[x+1]):
            return False

    return True


def getAnswer():
    correctPassword = 0
    for password in passwordsToTry:
        if hasTwoSameAdjacentDigit(str(password)) and isIncreasing(str(password)):
            correctPassword += 1

    return correctPassword


def main():
    print(getAnswer())


if __name__ == "__main__":
    main()
