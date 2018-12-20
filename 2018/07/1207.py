# Imports
from collections import defaultdict, namedtuple
from itertools import chain
import re
import heapq

# Matrix representation
class Matrix(object):
    # 2D array representation
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = defaultdict(list)
        for e in edges:
            self.addEdge(e.src, e.dst)

    def outgoing(self, n):
        return self.edges[n]

    def incoming(self, n):
        return [src for src, dstList in self.edges.items() if (n in dstList)]

    def addEdge(self, src, dst):
        self.edges[src].append(dst)

    def removeEdge(self, src, dst):
        if (dst in self.outgoing(src)):
            self.edges[src].remove(dst)

# custom objects
Req = namedtuple('Req', ['src', 'dst'])

# custom functions
def parse(s):
    matched = re.search('Step (.) .* step (.)', s)
    return matched.group(1), matched.group(2)

# Read & parse input into in-mem matrix data structure
with open('./1207.in', 'r') as f:
    reqs = [Req(*parse(l.strip())) for l in f.readlines()]

nodes = set()
for r in reqs:
    nodes.add(r.src)
    nodes.add(r.dst)

m = Matrix(nodes, reqs)

# TODO: graphical representation



#####################################
# Part 1 - Topological sort + break ties with alphabetical
#####################################

# Topological sort -> Kahn's algorithm
zeroIncoming = [n for n in m.nodes if len(m.incoming(n)) == 0]
heapq.heapify(zeroIncoming)

finalSeq = []

while (zeroIncoming):
    # Pop 1 - breaking tie by alphabetical order (using heap)
    currZeroIncoming = heapq.heappop(zeroIncoming)
    finalSeq.append(currZeroIncoming)
    dstNodes = list(m.outgoing(currZeroIncoming))
    for dst in dstNodes:
        m.removeEdge(currZeroIncoming, dst)
        if (len(m.incoming(dst)) == 0):
            heapq.heappush(zeroIncoming, dst)

print(''.join(finalSeq))


#####################################
# Part 2
#####################################



#####################################
# Lessons
#####################################

'''
'''
