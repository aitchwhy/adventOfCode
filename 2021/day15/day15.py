

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
        self.START = (0, 0)
        self.END = (self.yDim-1, self.xDim-1)

    def __repr__(self) -> str:
        finalStr = "##########\n"
        finalStr += f"xDim : {self.xDim} --- yDim: {self.yDim}\n"
        finalStr += "##########\n"
        for row in self.g:
            finalStr += ("|".join(str(x) for x in row) + "\n")
        finalStr += "##########"
        return finalStr

    # Total paths. (()! / ()!()!)

    # Naive solution - DFS.
    def dfs(self):
        # current path tracked til BEFORE current.
        path = []
        finalPathsWithRiskSum = []
        minRisk, minRiskPath = float("inf"), None

        # Since no NEGATIVE numbers, if revisit a node, then more costly than just 1 pass.
        # if visited, do not visit.
        def traverse(currNode):
            nonlocal minRisk, minRiskPath, path, finalPathsWithRiskSum
            assert currNode is not None, f"should NOT visit NULL currNode"

            # visit curr (do not visit if visited)
            if (currNode in path):
                return

            path.append(currNode)

            # Reached end
            if (currNode == self.END):
                # risk does NOT count start.
                currPathRiskSum = sum([self.g[n[1]][n[0]] for n in path[1:]])

                if (currPathRiskSum < minRisk):
                    minRisk = currPathRiskSum
                    minRiskPath = path.copy()
                finalPathsWithRiskSum.append((path.copy(), currPathRiskSum))
                # unvisit curr
                path.pop()
                return

            # neighbors
            offsets = ((0, 1), (1, 0))  # bottom, right ONLY
            for o in offsets:
                nextNode = (currNode[0] + o[0], currNode[1] + o[1])
                isInBoundary = (
                    (0 <= nextNode[0] < self.xDim) and (0 <= nextNode[1] < self.yDim))
                if isInBoundary:
                    # visit next
                    traverse(nextNode)

            # unvisit curr (cleanup)
            path.pop()

        # Start at top-left
        traverse(self.START)

        return minRisk, minRiskPath

    # DP (memoized solution)
    def dp(self):
        pass


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
    minRisk, minRiskPath = graph.dfs()
    print(f"minRisk: {minRisk} --- minRiskPath: {minRiskPath}")

    # part 2.
