##############################################
# Q1 --- find sum of all inputs
##############################################

# Read input - (f.read() for char-by-char read) & (loop file object for LINE-by-LINE reading)

with open('./1201.in', 'r') as f:
    freqList = [line.strip() for line in f]

# Compute sum
from functools import reduce
summed = reduce(lambda acc, curr: acc + int(curr), freqList, 0)

# print(summed)

##############################################
# Q1 --- find first cumulative value that repeats
# --- use itertools (efficient looping) : cycle!! because need to REPEAT given input indefinitely
##############################################

from itertools import cycle
cumulative, visited = 0, set()
for n in cycle(freqList):
    # print(summed)
    visited.add(cumulative)
    cumulative += int(n)
    # print(cumulative)
    if (cumulative in visited):
        print(cumulative)
        break

