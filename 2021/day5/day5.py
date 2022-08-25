
# x : left<>right
# y : top<>bottom
class Board():
    def __init__(self, allLines):
        # consider only straight lines + diagonal lines
        lines = [l for l in allLines if (l.isStraight() or l.isDiagonal())]
        # print(f"--------- lines: {lines}")

        xLen, yLen = float('-inf'), float('-inf')
        for l in lines:
            x1, y1 = l.start
            x2, y2 = l.end
            xLen = max(xLen, x1, x2)
            yLen = max(yLen, y1, y2)
        self.xLen = xLen+1
        self.yLen = yLen+1
        self.board = [([0] * (xLen+1)) for _ in range(yLen+1)]
        print(f"xLen: {xLen}, yLen: {yLen}")

        for l in lines:
            x1, y1 = l.start
            x2, y2 = l.end
            print(f"x : {x1},{y1}, y: {x2},{y2}")
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    self.board[y][x1] += 1
            elif y1 == y2:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    self.board[y1][x] += 1
            else:
                xStep = (1, 0) if ((x2 - x1) > 0) else (-1, 0)
                yStep = (0, 1) if ((y2 - y1) > 0) else (0, -1)
                curr = [x1, y1]
                while (curr != [x2, y2]):
                    self.board[curr[1]][curr[0]] += 1
                    curr[0] += xStep[0]
                    curr[1] += yStep[1]
                self.board[y2][x2] += 1

            # print("#########")
            # print(self)
            # print("#########")

    def getSpotCount(self, x, y):
        return self.board[y][x]

    def getSpotsWithCountAtLeast(self, minCount):
        spots = []
        for xIdx in range(self.xLen):
            for yIdx in range(self.yLen):
                spotCount = self.getSpotCount(yIdx, xIdx)
                # print(f"x: {xIdx}, y: {yIdx} === spot count : {spotCount}")
                if spotCount >= minCount:
                    spots.append((xIdx, yIdx))
        return spots

    def __repr__(self) -> str:
        return "\n".join([" ".join([str(x) for x in row]) for row in self.board])


class Line():
    def __init__(self, lineStr):
        # Split start, end by "->" and then split by ",".
        lineInfo = []
        for l in lineStr.split("->"):
            lineInfo.append([int(x) for x in l.strip().split(",")])
        self.start, self.end = lineInfo

    def isStraight(self):
        return ((self.start[0] == self.end[0] and self.start[1] != self.end[1])
                or (self.start[0] != self.end[0] and self.start[1] == self.end[1]))

    def isDiagonal(self):
        return abs(self.start[0] - self.end[0]) == abs(self.start[1] - self.end[1])

    def __repr__(self) -> str:
        return f"{self.start}->{self.end}"


def solve(inputLines):
    # parse input lines
    print("hello")

    # part 1 - find number of dots where 2+ lines overlap

    lines = [Line(l) for l in inputLines]
    # print(lines)
    board = Board(lines)
    # print(board)
    count = board.getSpotsWithCountAtLeast(2)
    print(f"spots with min count (len:{len(count)})")

    # part 2
