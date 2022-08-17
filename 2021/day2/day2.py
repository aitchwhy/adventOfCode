

# Class to hold state
from collections import namedtuple
from lib2to3.pgen2 import token
# SubState = namedtuple('SubState', ("depth", "dist"))


class SubState:
    def __init__(self, depth, dist, aim):
        self.depth = depth
        self.dist = dist
        self.aim = aim

    def __str__(self):
        return f"{self.depth} {self.dist} {self.aim}"


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
    part1State = SubState(0, 0, 0)
    for l in lineContents:
        parsed = parseLine(l)
        amt = parsed[1]
        if parsed[0] == FORWARD:
            part1State.dist += amt
            part1State.depth += (part1State.aim * amt)
        elif parsed[0] == UP:
            part1State.aim -= amt
        elif parsed[0] == DOWN:
            part1State.aim += amt

    print(part1State, part1State.dist * part1State.depth)

    # part 2
