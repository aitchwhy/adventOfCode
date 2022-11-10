
class Node():
    START, END = "start", "end"

    def __init__(self, name) -> None:
        self.name = name
        self.isSmall = self.name.islower()
        self.isBig = self.name.isupper()

    def isSmallCave(self):
        return self.isSmall

    def isBigCave(self):
        return self.isBig

    def isStart(self):
        return self.name == Node.START

    def isEnd(self):
        return self.name == Node.END


# Undirected graph
class Graph():
    # Adjacency list (not 2d matrix) - since likely to be sparse.
    def __init__(self) -> None:
        self.graph: dict[str, set] = dict()

    def getNodeNeighbors(self, node):
        if not (node in self.graph):
            self.graph[node] = set()
        return self.graph[node]

    def addEdge(self, node1, node2):
        node1Neighbors = self.getNodeNeighbors(node1)
        node2Neighbors = self.getNodeNeighbors(node2)

        # add node1->node2
        self.addNeighbor(node1, node2)

        # add node2->node1
        self.addNeighbor(node2, node1)

    def nodesAreNeighbors(self, node1, node2):
        return (node2 in self.getNodeNeighbors(node1)) and (node2 in self.getNodeNeighbors(node1))

    def addNeighbor(self, node, neighbor):
        self.getNodeNeighbors(node).add(neighbor)

    @staticmethod
    def parseEdgeStr(edgeStr):
        return edgeStr.split("-")


# use DFS backtracking to find all possible paths


def solve(lineContents):
    # print(lineContents)
    for l in lineContents:
        print(l)
