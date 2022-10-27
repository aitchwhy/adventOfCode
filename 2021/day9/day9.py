
class Map():
    OFFSETS = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def __init__(self, lines) -> None:
        mapMatrix = []
        for l in lines:
            mapMatrix.append(list(l))
        self.mapMatrix = mapMatrix
        self.yMax = len(mapMatrix)
        self.xMax = len(mapMatrix[0])

    def getHeight(self, x, y):
        return int(self.mapMatrix[y][x])

    def isInBound(self, x, y):
        return x >= 0 and x < self.xMax and y >= 0 and y < self.yMax

    def getNeighbors(self, x, y):
        neighbors = []
        for offset in self.OFFSETS:
            newX = x + offset[0]
            newY = y + offset[1]
            if self.isInBound(newX, newY):
                neighbors.append((newX, newY))
        return neighbors

    def getRisk(self, x, y):
        # height plus 1
        return int(self.getHeight(x, y)) + 1

    def __repr__(self) -> str:
        finalStr = "######\n"
        for l in self.mapMatrix:
            finalStr += ("".join(l) + "\n")
        finalStr += "######"
        return finalStr


def parseEntry(lineContents):
    return Map(lineContents)


def solve(lineContents):
    print(lineContents)

    # parse entry (2d matrix with height (int))
    mapMat = parseEntry(lineContents)
    print(mapMat)

    # print(mapMat.getHeight(0, 3))
    # print(mapMat.getHeight(2, 4))

    # print(mapMat.getNeighbors(0, 3))
    # print(mapMat.getNeighbors(2, 3))

    # part 1. Find all low points and get risk sum of all low points.
    riskSum = 0
    for x in range(mapMat.xMax):
        for y in range(mapMat.yMax):
            currHeight = mapMat.getHeight(x, y)
            neighbors = mapMat.getNeighbors(x, y)
            if all(mapMat.getHeight(*n) > currHeight for n in neighbors):
                riskSum += mapMat.getRisk(x, y)

    print(riskSum)
