def main():
    sum = 0
    lines = open("input1-2.txt").readlines()
    for line in lines:
        sum += calculateFuel(int(line))

    print(sum)


def calculateFuel(mass):
    fuel = mass//3-2
    if fuel > 0:
        return fuel+calculateFuel(fuel)
    return 0


if __name__ == "__main__":
    main()
