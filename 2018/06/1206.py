# imports
from collections import namedtuple, Counter, deque

# Helper classes
Pos = namedtuple('Pos', ['x','y'])

class Cell():
    # Class vars (shared)
    def __init__(self, x, y):
        # self.id = (x*y)
        self.p = Pos(int(x),int(y))
        self.closest = None
        self.distSum = 0

    def __repr__(self):
        return "({},{})".format(self.p.x, self.p.y)

    def __eq__(self, other):
        return (self.p == other)
        # return ((self.p.x == other.x) and (self.p.y == other.y))

# Helper functions
def manDist(p1, p2):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)

# Read file
with open('./1206.in', 'r') as f:
    posList = [Pos(*map(int, l.strip().split(', '))) for l in f.readlines()]

# Create Matrix of cells
top, bottom = 0, max([p.x for p in posList])
left, right = 0, max([p.y for p in posList])
matrix = [[Cell(row, col) for row in range(top, bottom+1)] for col in range(left, right+1)]

###############################################
# 1 - Find largest non-infinite area (of given coord)
###############################################

for row in matrix:
    for cell in row:
        dists = [(p, manDist(cell.p, p)) for p in posList]
        closest = [p for p,d in dists if (d == min(x[1] for x in dists))]
        if (1 == len(closest)):
            cell.closest = closest[0]

# Do not consider - infinite areas (which I find by finding set() of edge cell closeList)
edges = []
# Top / Bottom
edges.extend([matrix[0][colIdx].closest for colIdx in range(len(matrix[0]))])
edges.extend([matrix[len(matrix)-1][colIdx].closest for colIdx in range(len(matrix[0]))])
# Left / Right
edges.extend([matrix[rowIdx][0].closest for rowIdx in range(len(matrix))])
edges.extend([matrix[rowIdx][len(matrix[0])-1].closest for rowIdx in range(len(matrix))])
edgesSet = set([e for e in edges if (e != None)])

# Compute area for each 'pos'
c = Counter([cell.closest for row in matrix for cell in row if (cell.closest not in edgesSet)])
print(c)

###############################################
# 2 - Size of region (list of cells) with all cells sum(dist to each pos) < 10000
###############################################

for row in matrix:
    for cell in row:
        cell.distSum = sum([manDist(cell.p, p) for p in posList])

distCounter = Counter([cell.distSum for row in matrix for cell in row])
# Filter distSum < 10000, then 
safeRegionArea = sum([c[1] for c in distCounter.items() if c[0] < 10000])
print(safeRegionArea)

# 1081 - too low





###############################################
# Lessons
###############################################


'''



Related to Voronoi diagram
'''






# def printMat(m):
#     for row in m:
#         strRepr = []
#         for cell in row:
#             if (len(cell.closeList) == 0):
#                 strRepr.append('x')
#             elif (len(cell.closeList) == 1):
#                 strRepr.append(closeList[0])
#             else:
#                 strRepr.append('.')
#         print(''.join(strRepr))


