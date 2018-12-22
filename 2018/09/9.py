##########################
# Imports
##########################
import fileinput
import re
from itertools import cycle
from collections import deque

##########################
# Read input - 10 players; last marble is worth 1618 points: high score is 8317
##########################
gameInfo = []
for line in fileinput.input():
    matched = re.search(r'(\d+) players.* (\d+) points.*', line)
    gameInfo.append([int(matched.group(1)), int(matched.group(2))])


##########################
# part 1 - find max score
##########################


def playGame(numPlayers, numPoints):
    scores = [0] * numPlayers
    # Keep "curr" marble at end-idx of deque
    game = deque([0])
    for point in range(1, numPoints+1):
        if (point % 23 == 0):
            game.rotate(7)
            scores[(point % numPlayers)] += (point + game.pop())
            game.rotate(-1)
        else:
            game.rotate(-1)
            game.append(point)
    return max(scores)

for g in gameInfo:
    print(playGame(g[0], g[1]))


##########################
# part 2 - find max score (if last marble 100 times larger)
##########################

print(playGame(gameInfo[-1][0], gameInfo[-1][1] * 100))



'''
Lessons

(1) Using Deque REALLY speeds up the process (append / pop are O(1) operations instead of O(N))
(2) It is convenient to have HEAD of CIRCULAR data structures at **END** of the list ---> makes append / pop conceptually easier relative positions to head

'''

