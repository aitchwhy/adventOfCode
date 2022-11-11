

class Grid():
    DOT, EMPTY = "#", "."

    from enum import Enum

    class Section(Enum):
        DOT = 1
        FOLD = 2

    def __init__(self, lines) -> None:
        dots, folds, maxX, maxY = Grid.parseInput(lines)
        self.xDim = maxX+1
        self.yDim = maxY+1
        self.grid = [[Grid.EMPTY] * self.xDim for _ in range(self.yDim)]
        self.dots = dots
        for dot in dots:
            self.grid[dot[1]][dot[0]] = Grid.DOT
        self.folds = folds

    @staticmethod
    def parseInput(lines):
        dots = []
        folds = []
        maxX, maxY = float("-inf"), float("-inf")
        CURR_SECTION = Grid.Section.DOT
        for l in lines:
            # Dot section parsing.
            if CURR_SECTION == Grid.Section.DOT:
                if l == "":
                    CURR_SECTION = Grid.Section.FOLD
                    continue
                coords = l.split(",")
                x, y = int(coords[0]), int(coords[1])
                maxX, maxY = max(maxX, x), max(maxY, y)
                dots.append((x, y))

            # Fold section parsing.
            elif CURR_SECTION == Grid.Section.FOLD:
                # split(splitStr, maxSplit) -> maxSplit determines max split count.
                # If maxSplit is 1, then split only once -> which is what we want here.
                foldSplits = l.split("fold along ", 1)
                foldLineStr = foldSplits[1]
                foldAxis, foldAxisPos = foldLineStr.split("=")
                folds.append((foldAxis, int(foldAxisPos)))

        return dots, folds, maxX, maxY

    def __repr__(self) -> str:
        finalStr = "##############\n"
        for l in self.grid:
            finalStr += ("".join(l) + "\n")
        finalStr += "##############\n"
        finalStr += f"dims (x,y) : {(self.xDim, self.yDim)}\n"
        finalStr += "##############\n"
        finalStr += f"dots : {self.dots}\n"
        finalStr += "##############\n"
        finalStr += f"Folds : {self.folds}\n"
        finalStr += "##############"
        return finalStr

    def fold(self, foldInfo) -> None:
        foldAxis, foldAxisPos = foldInfo

        # remove fold line. Then merge flipped halfs.
        # Then resize grid (xDim, yDim, grid)
        if foldAxis == "y":
            # horizontal fold.
            # TODO: not sure if this fold logic is correct, what happens when not equal halves?
            newXDim = self.xDim
            newYDim = (foldAxisPos)
            newGrid = [[Grid.EMPTY] * newXDim for _ in range(newYDim)]
            # fill in dots from both halves of fold.
            newDots = []
            for dot in self.dots:
                dotX, dotY = dot
                # top half -> fill as original
                newDotX, newDotY = dotX, dotY
                if dotY < foldAxisPos:
                    newDotX, newDotY = dotX, dotY
                elif dotY > foldAxisPos:
                    # bottom half -> fill as flipped
                    # (0, 13) -> folded y=7 -> (0, 1)
                    # (15 ydim - 1) - (13 dotY) = 1
                    flippedDotY = (self.yDim - 1) - dotY
                    newDotX, newDotY = dotX, flippedDotY
                # fill new dot
                newGrid[newDotY][newDotX] = Grid.DOT
                newDots.append((newDotX, newDotY))
            # update to new grid.
            self.grid = newGrid
            self.xDim = newXDim
            self.yDim = newYDim
            self.dots = newDots
        elif foldAxis == "x":
            # vertical fold.

            # TODO: not sure if this fold logic is correct, what happens when not equal halves?
            newXDim = (foldAxisPos)
            newYDim = self.yDim
            newGrid = [[Grid.EMPTY] * newXDim for _ in range(newYDim)]
            newDots = []
            # fill in dots from both halves of fold.
            for dot in self.dots:
                dotX, dotY = dot
                newDotX, newDotY = dotX, dotY
                # left half -> fill as original
                if dotX < foldAxisPos:
                    newDotX, newDotY = dotX, dotY
                elif dotX > foldAxisPos:
                    # right half -> fill as flipped
                    flippedDotX = (self.xDim - 1) - dotX
                    newDotX, newDotY = flippedDotX, dotY
                # fill new dot
                newGrid[newDotY][newDotX] = Grid.DOT
                newDots.append((newDotX, newDotY))

            # update to new grid.
            self.grid = newGrid
            self.xDim = newXDim
            self.yDim = newYDim
            self.dots = newDots

    def getDotCount(self) -> int:
        from itertools import chain
        return list(chain(*self.grid)).count(Grid.DOT)


def solve(lineContents):
    print("------- printing line contents")
    print(lineContents)

    # parse input.
    # dots -> (x,y) where x (left->right) y (top->bottom). top-left is (0,0)
    # fold -> fold paper. y=N is horizontal fold, x=M is vertical fold.
    # - after fold, that line disappears + dots are merged.
    grid = Grid(lineContents)
    print("------ Printing grid")
    print(grid)
    print(grid.getDotCount())

    for idx, f in enumerate(grid.folds):
        if (idx == 1):
            break
        print(f"------ Printing grid after fold {f}")
        grid.fold(f)
        print(grid)
        print(grid.getDotCount())

    # part 1. How many dots are left after 1st folding?

    # part 2.
