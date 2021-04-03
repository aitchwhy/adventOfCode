import fileinput
import re
from collections import namedtuple
from itertools import count

Point = namedtuple('Point', ['x', 'y', 'dx', 'dy'])
stars = []
for l in fileinput.input():
    matched = re.search(r'position=<\ *(-?\d+),\ *(-?\d+)>\ *velocity=<\ *(-?\d+),\ *(-?\d+)>', l)
    stars.append(Point(*map(int, matched.group(1,2,3,4))))

# State after time 't'
def state(t):
    return [Point(s.x+t*s.dx, s.y+t*s.dy, s.dx, s.dy) for s in stars]

def boundingBox(state):
    # left, right, top, bottom
    return min([s.x for s in state]),max([s.x for s in state]),min([s.y for s in state]),max([s.y for s in state])

def boundingArea(box):
    return (box[1] - box[0]) * (box[3] - box[2])

def printSky(state):
    left, right, top, bottom = boundingBox(state)
    sky = [[' ' for _ in range(left, right+1)] for _ in range(top, bottom+1)]
    for s in state:
        sky[s.y-top][s.x-left] = '*'

    for row in sky:
        print(''.join(row))

####################################
# Part 1
####################################
minArea, minAreaTime, prevArea = float('inf'), -1, float('inf')
for t in count():
    currSky = state(t)
    currBox = boundingBox(currSky)
    currBoxArea = boundingArea(currBox)
    if (currBoxArea < minArea): minArea, minAreaTime = boundingArea(currBox), t
    if (currBoxArea > prevArea): break
    prevArea = currBoxArea

print(minArea, minAreaTime)
printSky(state(minAreaTime))


####################################
# Part 2
####################################


print(minAreaTime)
