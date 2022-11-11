

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
        finalStr += f"Folds : {self.folds}"
        finalStr += "##############"
        return finalStr

    def fold(self):
        pass

    def getDotCount(self) -> int:
        from itertools import chain
        oneDimGrid = chain(*self.grid)
        print(self.grid)
        print(oneDimGrid)
        return 0


def solve(lineContents):
    print("------- printing line contents")
    print(lineContents)

    # parse input.
    grid = Grid(lineContents)
    print("------ Printing grid")
    print(grid)
    # dots -> (x,y) where x (left->right) y (top->bottom). top-left is (0,0)
    # fold -> fold paper. y=N is horizontal fold, x=M is vertical fold.
    # - after fold, that line disappears + dots are merged.

    # part 1. How many dots are left after 1st folding?

    # part 2.
