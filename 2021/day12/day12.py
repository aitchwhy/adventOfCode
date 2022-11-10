
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

    def __repr__(self) -> str:
        return f"({self.name})"

    # Need to equate same "name" nodes as equal.
    # Otherwise, set() of neighbors does not work.
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Node):
            return False
        return self.name == other.name

    # To make Node() hashable, need to define __hash__.
    def __hash__(self) -> int:
        return hash(self.name)


# Undirected graph
class Graph():
    # Adjacency list (not 2d matrix) - since likely to be sparse.
    def __init__(self) -> None:
        self.graph: dict[Node, set] = dict()

    def getNodeNeighbors(self, node):
        if not (node in self.graph):
            self.graph[node] = set()
        return self.graph[node]

    def addEdge(self, node1: Node, node2: Node):
        node1Neighbors = self.getNodeNeighbors(node1)
        node2Neighbors = self.getNodeNeighbors(node2)

        # add node1->node2
        self.addNeighbor(node1, node2)

        # add node2->node1
        self.addNeighbor(node2, node1)

    def nodesAreNeighbors(self, node1, node2) -> bool:
        return (node2 in self.getNodeNeighbors(node1)) and (node2 in self.getNodeNeighbors(node1))

    def addNeighbor(self, node, neighbor):
        self.getNodeNeighbors(node).add(neighbor)

    def parseEdgeStr(self, edgeStr):
        nodes = edgeStr.split("-")
        self.addEdge(Node(nodes[0]), Node(nodes[1]))

    def __repr__(self) -> str:
        keys = self.graph.keys()
        # finalStr = " |" + "|".join(keys)
        finalStr = "#################\n"
        for key in keys:
            neighbors = self.getNodeNeighbors(key)
            finalStr += f"{key}: {(self.getNodeNeighbors(key))}\n"
        finalStr += "#################"
        return finalStr

    def DFS(self):
        # use DFS backtracking to find all possible paths (start) -> (end).
        paths = []

        # Find start Node.
        startNode = [n for n in self.graph.keys() if n.isStart()][0]
        endNode = [n for n in self.graph.keys() if n.isEnd()][0]

        # backtracking DFS.
        # TODO: With recursion
        currPath = []

        def traverse(node):
            nonlocal paths, currPath

            # print(node, currPath)

            # exit if already visited (in curr Path & small cave)
            if (node in currPath) and (node.isSmallCave()):
                return

            # if len(currPath) > 10:
            #     return

            # Visit current node
            currPath.append(node)
            if node.isEnd():
                # found path to end
                # print(f"~~~~~~found path to end : {currPath}")
                paths.append(currPath.copy())
                currPath.pop()
                return

            # Traverse all neighbors of current node.
            for neighbor in self.getNodeNeighbors(node):
                # Traverse neighbor
                traverse(neighbor)

            # leave / backtrack current node
            currPath.pop()

        traverse(startNode)

        # TODO: without recursion

        # currPaths = [startNode]
        # # do NOT put "big" caves into the - no need to check.
        # while len(currPaths) > 0:
        #     # process curr top of stack - current list of nodes (path).
        #     currPath = currPaths.pop()
        #     # Get curr neighbors. Only non-visited ones.
        #     currNeighbors = [n for n in self.getNodeNeighbors(
        #         currPath) if (n not in visited)]

        #     # mark curr node as visited. Only if not "big" cave.
        #     if currPath.isSmallCave():
        #         visited.add(currPath)

        return paths


def solve(lineContents):
    # print(lineContents)

    # parse input
    g = Graph()
    for l in lineContents:
        print(l)
        g.parseEdgeStr(l)
    print(f"Printing Graph")
    print(g)

    paths = g.DFS()
    print(f"########### Printing paths")
    print(*paths, sep="\n")
    print(f"num paths found : {len(paths)}")

    # part 1. Find all possible paths from start to end (visiting small caves once).

    # part 2.
