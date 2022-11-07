

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

    def __add__(self, otherGrid) -> None:
        # Note : Assuming 2 grids match in dimensions.
        xLen = len(self.grid)
        yLen = len(self.grid[0])
        for xIdx in range(xLen):
            for yIdx in range(yLen):
                self.grid[xIdx][yIdx] += otherGrid.grid[xIdx][yIdx]

    def get(self, x, y) -> int:
        return self.grid[y][x]

    def set(self, x, y, val):
        self.grid[y][x] = val


class EnergyState(Grid):
    def __init__(self, initValueStrs) -> None:
        super().__init__(10, 10)

        for yIdx, line in enumerate(initValueStrs):
            for xIdx, char in enumerate(line):
                self.set(xIdx, yIdx, int(char))

    # def __repr__(self) -> str:
    #     return super().__repr__()


class EnergyDelta(Grid):
    def __init__(self) -> None:
        super().__init__(10, 10)

    # def __repr__(self) -> str:
    #     return super().__repr__()

    def isEmpty(self) -> bool:
        '''
        Check if ALL energy is 0 -> return True
        '''
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
