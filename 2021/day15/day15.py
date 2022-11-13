

# 2 approaches
# Naive -> DFS search from start-end and get min dist.
# DP -> for each cell, compute smallest from curr-end. Re-use prev calculated (e.g. min dist from cells closer to end)

class Graph():
    # X : left<>right (left = 0)
    # Y : top<>bottom (top = 0)
    def __init__(self, lines) -> None:
        self.xDim = len(lines[0])
        self.yDim = len(lines)
        self.g = [[0] * self.xDim for _ in range(self.yDim)]
        for xIdx in range(self.xDim):
            for yIdx in range(self.yDim):
                self.g[yIdx][xIdx] = int(lines[yIdx][xIdx])

    def __repr__(self) -> str:
        finalStr = "##########\n"
        for row in self.g:
            finalStr += ("|".join(str(x) for x in row) + "\n")
        finalStr += "##########"
        return finalStr


def solve(lines):
    # parse input
    # 2D map. Start top-left, end bottom-right.
    # Can ONLY move 4 dirs (no diagonal)
    # Each cell number = risk level (int)
    # NOT count 1st cell (only risk incurred if "ENTERED")

    # part 1. Find path with SMALLEST risk total.
    print(lines)
    graph = Graph(lines)
    print(graph)

    # part 2.
