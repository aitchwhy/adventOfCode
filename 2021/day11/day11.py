

# TODO: custom Grid "+" operator to add 2 grids together.
# https://www.codingem.com/python-__add__-method/


class Grid():
    OFFSETS = [(1, 0), (-1, 0), (0, 1), (0, -1),
               (-1, -1), (-1, 1), (1, -1), (1, 1)]
    # 2D grid.
    # For debug convenience, "x" is left<>right index (leftside 0)
    # For debug convenience, "y" is top<>down index (topside 0)

    def __init__(self, xLen, yLen) -> None:
        self.xLen = xLen
        self.yLen = yLen
        self.grid = [[0]*(xLen) for _ in range(yLen)]

    def __repr__(self) -> str:
        # 2d grid repr string
        finalStr = "######\n"
        for l in self.grid:
            finalStr += ("".join([str(x) for x in l]) + "\n")
        finalStr += "######"
        return finalStr

    def __add__(self, otherGrid):
        # Note : Assuming 2 grids match in dimensions.
        for xIdx in range(self.xLen):
            for yIdx in range(self.yLen):
                self.grid[xIdx][yIdx] += otherGrid.grid[xIdx][yIdx]
        return self

    def get(self, x, y) -> int:
        return self.grid[y][x]

    def set(self, x, y, val):
        self.grid[y][x] = val

    def isInBoundary(self, x, y) -> bool:
        return (0 <= x < len(self.grid[0]) and 0 <= y < len(self.grid))

    def getNeighbors(self, x, y):
        neighbors = []
        for offset in self.OFFSETS:
            neighborX, neighborY = x + offset[0], y + offset[1]
            if self.isInBoundary(neighborX, neighborY):
                neighbors.append((neighborX, neighborY))
        return neighbors

    def setAll(self, val):
        for xIdx in range(self.xLen):
            for yIdx in range(self.yLen):
                self.set(xIdx, yIdx, val)

    def incrAll(self):
        for xIdx in range(self.xLen):
            for yIdx in range(self.yLen):
                self.set(xIdx, yIdx, self.get(xIdx, yIdx)+1)

    def isEmpty(self) -> bool:
        '''
        Check if ALL energy is 0 -> return True
        '''
        for xIdx in range(self.xLen):
            for yIdx in range(self.yLen):
                if self.get(xIdx, yIdx) != 0:
                    return False
        return True


class EnergyState(Grid):

    def __init__(self, initValueStrs) -> None:
        super().__init__(10, 10)
        self.flashed = [[False]
                        * (self.xLen) for _ in range(self.yLen)]

        for yIdx, line in enumerate(initValueStrs):
            for xIdx, char in enumerate(line):
                self.set(xIdx, yIdx, int(char))

    def runStep(self):
        # Incr all cells by 1.
        self.incrAll()

        # Flash all cells > 9
        keepFlashing = True
        totalFlashCount = 0
        while keepFlashing:
            flashedCount = self.flash()
            totalFlashCount += flashedCount
            keepFlashing = (flashedCount > 0)

        # reset flashed back to not flashed + set to 0
        self.resetFlashed()
        return totalFlashCount

    def flash(self):
        # for all > 9 cells - set current cell as "flashed"
        flashCount = 0
        for xIdx in range(self.xLen):
            for yIdx in range(self.yLen):
                notFlashed = (self.flashed[yIdx][xIdx] == False)
                if (self.get(xIdx, yIdx) > 9) and (notFlashed):
                    # Process flash neighbors
                    for n in self.getNeighbors(xIdx, yIdx):
                        self.set(n[0], n[1], self.get(n[0], n[1])+1)
                    # set to "flashed"
                    self.flashed[yIdx][xIdx] = True
                    flashCount += 1
        return flashCount

    def resetFlashed(self):
        # reset all "flashed" cells to not flashed + set to 0
        for xIdx in range(self.xLen):
            for yIdx in range(self.yLen):
                if self.flashed[yIdx][xIdx]:
                    self.flashed[yIdx][xIdx] = False
                    self.set(xIdx, yIdx, 0)


def solve(lineContents):
    print(f"day 11 lineContents : {lineContents}")

    # TODO: Parse input (10x10) grid where each cell is octopus energy level.

    # Each step,
    # - EACH octopus energy +1.
    # - if energy > 9, "flash" occurs (all 8 adjacent +1 energy) and
    # - "flash" loop until no more
    # - When no more "flash" -> those who "flashed" energy = 0.

    # Note: feels like setting to 0 at end is deliberate wording. But NVM for now.
    # Can set to 0 right after "flash" occurs.

    # part 1. given initial state, how many TOTAL flashes after 100 steps?
    # TODO: 2 10x10 grids.
    # - "energyStates" : One for current energy state
    # - "energyDeltas" : one for 1 iteration of energy delta to apply (result of "flash")
    #   - Use energyDeltas to update E state each loop - do while all delta != 0
    eState = EnergyState(lineContents)
    print(eState)

    # TODO: should be 1656 flashes after 100 steps.
    # totalFlashCount = 0
    # for stepIdx in range(100):
    #     print(f"step {stepIdx}")
    #     totalFlashCount += eState.runStep()
    #     print(f"totalFlashCount : {totalFlashCount}")
    #     print(eState)

    # part 2. Find first step when ALL octopus flash at same time.

    step = 1
    while True:
        print(f"step {step}")
        currStepFlashCount = eState.runStep()
        print(f"currStepFlashCount : {currStepFlashCount}")
        if (currStepFlashCount == (10*10)):
            break
        # print(eState)
        step += 1
