
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

    def findReachable(self, x, y, canMoveFunc):
        '''
        Find all reachable points by doing BFS starting from (x,y)

        canMoveFunc: (x1,y1,x2,y2) -> bool. Can tell if can move from (x1,y1) to (x2,y2)
        '''
        visited = set()

        from collections import deque
        toVisit = deque()
        toVisit.append((x, y))

        while len(toVisit) > 0:
            curr = toVisit.popleft()
            # visit curr
            if not curr in visited:
                # add neighbors
                for n in self.getNeighbors(curr[0], curr[1]):
                    if canMoveFunc(curr[0], curr[1], n[0], n[1]):
                        toVisit.append(n)
                visited.add(curr)
        return visited

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
    lowPoints = []
    for x in range(mapMat.xMax):
        for y in range(mapMat.yMax):
            currHeight = mapMat.getHeight(x, y)
            neighbors = mapMat.getNeighbors(x, y)
            # is low point (lower than all neighbors)
            if all(mapMat.getHeight(*n) > currHeight for n in neighbors):
                lowPoints.append((x, y))
                riskSum += mapMat.getRisk(x, y)

    print(f"riskSum : {riskSum} --- lowPoints : {lowPoints}")

    # part 2. Find all "basins" (points that flow to low points delineated by 9's).
    # Find largest 3 basins and multiply their areas.
    # size of basin is num(locations) within basin including low point.

    # Approach - find low points. from each low point, BFS to find all reachable until 9's.

    # TODO: sample -> basin sizes 3,9,14,9 (largest 3 mult = 1134)

    # can move to if NOT "9" and is higher number
    def canMoveTo(x1, y1, x2, y2):
        isHigherNum = mapMat.getHeight(x1, y1) < mapMat.getHeight(x2, y2)
        isNot9 = mapMat.getHeight(x2, y2) != 9
        return (isHigherNum and isNot9)

    # all basin sizes
    basinSizes = []
    # use heap to get max 3 basin sizes (min-heap)
    import heapq
    for lowPoint in lowPoints:
        lowX, lowY = lowPoint
        reachable = mapMat.findReachable(lowX, lowY, canMoveTo)
        # print(f"lowPoint : {lowPoint} --- reachable : {(reachable)}")
        heapq.heappush(basinSizes, -1 * len(reachable))

    print(basinSizes)

    final = 1
    for i in range(3):
        final *= (-1 * heapq.heappop(basinSizes))
    print(final)
