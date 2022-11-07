

# TODO: custom Grid "+" operator to add 2 grids together.
# https://www.codingem.com/python-__add__-method/

class Grid():
    # 2D grid.
    # For debug convenience, "x" is left<>right index (leftside 0)
    # For debug convenience, "y" is top<>down index (topside 0)
    def __init__(self, xLen, yLen) -> None:
        self.grid = [[0]*(xLen) for _ in range(yLen)]

    def __repr__(self) -> str:
        # TODO: 2d grid repr string
        finalStr = "######\n"
        for l in self.grid:
            finalStr += ("".join([str(x) for x in l]) + "\n")
        finalStr += "######"
        return finalStr

    def __add__(self, otherGrid):
        # Note : Assuming 2 grids match in dimensions.
        xLen = len(self.grid[0])
        yLen = len(self.grid)
        for xIdx in range(xLen):
            for yIdx in range(yLen):
                self.grid[xIdx][yIdx] += otherGrid.grid[xIdx][yIdx]
        return self

    def get(self, x, y) -> int:
        return self.grid[y][x]

    def set(self, x, y, val):
        self.grid[y][x] = val

    def isInBoundary(self, x, y) -> bool:
        return (0 <= x < len(self.grid[0]) and 0 <= y < len(self.grid))


class EnergyState(Grid):
    def __init__(self, initValueStrs) -> None:
        super().__init__(10, 10)

        for yIdx, line in enumerate(initValueStrs):
            for xIdx, char in enumerate(line):
                self.set(xIdx, yIdx, int(char))

    def setDelta(self, delta):
        # for all > 9 cells, set neighboring cells' deltas as 1.
        offsets = [(1, 0), (-1, 0), (0, 1), (0, -1),
                   (-1, -1), (-1, 1), (1, -1), (1, 1)]

        xLen = len(self.grid[0])
        yLen = len(self.grid)
        for xIdx in range(xLen):
            for yIdx in range(yLen):
                if self.get(xIdx, yIdx) > 9:
                    self.set(xIdx, yIdx, 0)
                    for offset in offsets:
                        if self.isInBoundary(xIdx+offset[0], yIdx+offset[1]):
                            delta.set(xIdx+offset[0], yIdx+offset[1], 1)


class EnergyDelta(Grid):
    def __init__(self) -> None:
        super().__init__(10, 10)

    def setAll(self, val):
        xLen, yLen = len(self.grid[0]), len(self.grid)
        for xIdx in range(xLen):
            for yIdx in range(yLen):
                self.set(xIdx, yIdx, val)

    def isEmpty(self) -> bool:
        '''
        Check if ALL energy is 0 -> return True
        '''
        xLen, yLen = len(self.grid[0]), len(self.grid)
        for xIdx in range(xLen):
            for yIdx in range(yLen):
                if self.get(xIdx, yIdx) != 0:
                    return False
        return True


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
    eDelta = EnergyDelta()

    print(eState)
    print(eDelta)

    # TODO: should be 1656 flashes after 100 steps.
    for stepIdx in range(2):
        eDelta.setAll(1)
        print(f"step {stepIdx}")
        while (not eDelta.isEmpty()):
            eState += eDelta
            # TODO: NOT WORKING to set "0" -> must be set 0 for WHOLE step.
            eDelta.setAll(0)
            eState.setDelta(eDelta)
        print(eState)
        print(eDelta)
