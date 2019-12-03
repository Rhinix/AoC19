class Wire:

    def __init__(self, wireInput=[]):
        self.lines = []
        x = 0
        y = 0
        for entry in wireInput:
            if entry[0] == "U":
                y += int(entry[1:])
            elif entry[0] == "D":
                y -= int(entry[1:])
            elif entry[0] == "R":
                x += int(entry[1:])
            elif entry[0] == "L":
                x -= int(entry[1:])
            else:
                print("ta mèreeeeeeeeeeeeeeee")
            startPoint = self.lines[-1].endPoint if len(self.lines) != 0 else Point(
                0, 0)
            endPoint = Point(x, y)
            newLine = Line(startPoint, endPoint)
            self.lines.append(newLine)


class Line:
    def __init__(self, startPoint, endPoint):
        self.startPoint = startPoint
        self.endPoint = endPoint

    def __repr__(self):
        return "\""+str(self.startPoint)+","+str(self.endPoint)+"\""

    def isVerticalWire(self):
        return self.startPoint.x == self.endPoint.x


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "x: "+str(self.x)+", y: "+str(self.y)


def main():
    inputFile = open("input.txt")
    firstWire = Wire(inputFile.readline().rstrip().split(","))
    secondWire = Wire(inputFile.readline().rstrip().split(","))
    print(f"firstWire.lines: { firstWire.lines}")
    print(f"secondWire.lines: { secondWire.lines}")
    intersection = createListOfintersection(firstWire, secondWire)
    print(intersection)


def createListOfintersection(firstWire, secondWire):
    intersections = []
    for i in range(0, len(secondWire)):
        if firstWire[i].lines.isVerticalWire() and secondWire[i].lines.isVerticalWire():
            intersections.append()
    return []


if __name__ == "__main__":
    main()
