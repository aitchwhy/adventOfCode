import heapq


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

    def getRisk(self, x, y):
        return self.g[y][x]

    def dijkstras(self):
        w, h = self.xDim, self.yDim

        # Dijkstra's Algorithm
        start = (0, 0)
        # shortest distances from start to this position
        shortestDistFromStart = {start: 0}
        visited = {}  # positions of all visited cells
        prev = {}

        #  priority queue initialized with the start and it's shortest distance
        heap = []
        # !! important - distance is first in the tuple
        heapq.heappush(heap, (0, start))

        while len(heap):

            minVal, index = heapq.heappop(heap)
            x, y = index

            visited[index] = True

            # get all adjacent neighors
            neighbors = [(x+dx, y+dy)
                         for dx, dy in [(0, -1), (-1, 0), (0, 1), (1, 0)]]
            # that are not out of bounds
            neighbors = [(x, y) for x, y in neighbors if x >=
                         0 and x < w and y >= 0 and y < h]
            # and not already visited
            neighbors = [
                neighbor for neighbor in neighbors if neighbor not in visited]

            if shortestDistFromStart[index] < minVal:
                continue

            for neighbor in neighbors:

                # calculate distance of this neighbor from start
                nx, ny = neighbor
                newDistance = shortestDistFromStart[index] + \
                    self.getRisk(nx, ny)
                # if this new distance is better or not set, set it and put this neighbor
                # on the queue
                if neighbor not in shortestDistFromStart or\
                        newDistance < shortestDistFromStart[neighbor]:
                    shortestDistFromStart[neighbor] = newDistance
                    prev[neighbor] = index
                    heapq.heappush(heap, (newDistance, neighbor))

        print(prev[(w-1, h-1)])
        return shortestDistFromStart[(w-1, h-1)]


def solve(lines):
    # parse input
    # 2D map. Start top-left, end bottom-right.
    # Can ONLY move 4 dirs (no diagonal)
    # Each cell number = risk level (int)
    # NOT count 1st cell (only risk incurred if "ENTERED")

    # part 1. Find path with SMALLEST risk total.
    # Naive way runs too long on puzzle input. (Finishes sample though).
    print(lines)
    graph = Graph(lines)
    print(graph)
    # minRisk, minRiskPath = graph.dfs()
    # print(f"minRisk: {minRisk} --- minRiskPath: {minRiskPath}")

    minRisk = graph.dijkstras()
    print(f"minRisk: {minRisk}")

    # Note : DP gave "714" -> "too low" (but somehow right answer for someone else)

    # part 2.
