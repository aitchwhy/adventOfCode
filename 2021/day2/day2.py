

# Class to hold state
from collections import namedtuple
from lib2to3.pgen2 import token
# SubState = namedtuple('SubState', ("depth", "dist"))


class SubState:
    def __init__(self, depth, dist):
        self.depth = depth
        self.dist = dist

    def __str__(self):
        return f"{self.depth} {self.dist}"


FORWARD, DOWN, UP = 'forward', 'down', 'up'


# Returns a tuple of tokens, fatally failing if invalid inputs.
def parseLine(l):
    tokens = [x for x in l.strip().split()]
    if len(tokens) != 2 or tokens[0] not in [FORWARD, DOWN, UP]:
        raise Exception(f"Invalid line: {l}")
    tokens[-1] = int(tokens[-1])
    return tokens


def solve(lineContents):
    # part 1 - calculate state after running all instructions.
    part1State = SubState(0, 0)
    for l in lineContents:
        parsed = parseLine(l)
        if parsed[0] == FORWARD:
            part1State.dist += parsed[1]
        elif parsed[0] == UP:
            part1State.depth -= parsed[1]
        elif parsed[0] == DOWN:
            part1State.depth += parsed[1]

    print(part1State, part1State.dist * part1State.depth)

    # part 2
