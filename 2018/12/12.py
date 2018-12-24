import fileinput
import re
from collections import defaultdict
from copy import deepcopy

EMPTY, PLANT = '.', '#'

lines = list(fileinput.input())

start = set(idx for idx,x in enumerate(lines[0].split()[-1]) if x == PLANT)
rules = dict(line.split()[::2] for line in lines[2:])

def step(state):
    # Check rule for range with Extra -2, +2 offset for min, max of plants
    # -> in "view" of existing plants (possible rule application)
    result = set()
    for potIdx in range(min(state)-2, max(state)+3):
        currPattern = ''.join([PLANT if (idx in state) else EMPTY for idx in range(potIdx-2, potIdx+3)])
        if (currPattern in rules) and (rules[currPattern] == PLANT):
            result.add(potIdx)
    return result

################################
# Part 1
################################

GEN_COUNT = 20
s = start
for g in range(GEN_COUNT):
    s = step(s)

print(sum(s))

################################
# Part 2
################################

GEN_COUNT_2 = 50000000000
# Pattern -> after first few (~ 1000) steps, increments constantly
prevSum, currSum = None, 0
s = start
for steps in range(1000):
    # prevSum = currSum
    s = step(s)
    # currSum = sum(s)
    prevSum, currSum = currSum, sum(s)

print(prevSum + (currSum - prevSum) * (GEN_COUNT_2 - steps))
