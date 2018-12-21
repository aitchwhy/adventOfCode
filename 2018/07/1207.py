# Imports
from collections import defaultdict, namedtuple, Counter, deque
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





NUM_WORKERS = 5

def workTime(c):
    return (ord(c) - ord('A') + 1) + 60


m2 = Matrix(nodes, reqs)
zeroIncoming = [n for n in m.nodes if len(m2.incoming(n)) == 0]
heapq.heapify(zeroIncoming)


# TODO: calculate todos
remWork = Counter({c:workTime(c) for c in finalSeq})

workAssignments = [[] for _ in range(NUM_WORKERS)]

doableWork = zeroIncoming.copy()
heapq.heapify(doableWork)

# May return 'None' if no available work
def finishWork():
    # Get zero-incoming (current work set) & update
    currZeroIncoming = heapq.heappop(zeroIncoming)
    dstNodes = list(m2.outgoing(currZeroIncoming))
    for dst in dstNodes:
        m2.removeEdge(currZeroIncoming, dst)
        if (len(m2.incoming(dst)) == 0):
            heapq.heappush(zeroIncoming, dst)
            heapq.heappush(doableWork, dst)

    # TODO: Append Snapshot "doableWork"
    with open('ass.txt', 'a') as f:
        f.write(''.join(doableWork) + '\n')


    # TODO: ???? Elim from new work -> if other worker doing work



while (sum(remWork.values()) > 0):
    # 1 iteration of work assignments (for each worker)

    # (1) Decrement - current assigned work as done
    if (len(workAssignments[0]) > 0):
        # Get new work when finishing up any work
        for works in workAssignments:
            if (works[-1] is not None):
                if (remWork[works[-1]] == 1):
                    # TODO: Append Snapshot "finished works"
                    with open('ass.txt', 'a') as f:
                        f.write('FINISHED : [{}]  '.format(works[-1]))
                    finishWork()
                # Decrement
                remWork.subtract([works[-1]])

    # (2) Assign work
    for workerId in range(NUM_WORKERS):
        currWorkerPrev = workAssignments[workerId][-1] if (len(workAssignments[workerId]) > 0) else None
        if (currWorkerPrev is not None) and (remWork[currWorkerPrev] > 0):
            # Continue old work
            workAssignments[workerId].append(currWorkerPrev)
        else:
            # Need new work (if work is available)
            if (len(doableWork) > 0):
                workAssignments[workerId].append(heapq.heappop(doableWork))
            else:
                workAssignments[workerId].append(None)

    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(remWork)

print(len(workAssignments[0]))

with open('ass.txt', 'a') as f:
    for w in workAssignments:
        f.write(' '.join([e if (e is not None) else "-" for e in w]) + '\n')


#####################################
# Lessons
#####################################

'''
(1) Topological sort -> Kahn's algorithm (requires removing edges while creating final topologically sorted list)
(2) Removing edges (list) while iterating ... makes iter SKIP! elements (need to make copy to iter while modify)
(3)

'''
