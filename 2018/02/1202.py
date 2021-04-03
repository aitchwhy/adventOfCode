###################################
# 1
###################################

# Read input
with open('./1202.in', 'r') as f:
    boxIds = [l.strip() for l in f.readlines()]

from collections import defaultdict
twoLetterIdCount, threeLetterIdCount = 0,0
for boxId in boxIds:
    charCounts = defaultdict(int)
    for c in boxId: charCounts[c] += 1
    # list of count values (find if 2,3 exists)
    counts = [v for k,v in charCounts.items()]
    twoLetterIdCount += (1 if (2 in counts) else 0)
    threeLetterIdCount += (1 if (3 in counts) else 0)

# Answer
# print(twoLetterIdCount * threeLetterIdCount)

###################################
# 2
###################################

# Find 2 correct boxIDs by finding 2 IDs differing by 1 char

def diffDist(s1, s2):
    # Narrow word dist def - only check each char at any matching index
    return sum([0 if (s1[idx] == s2[idx]) else 1 for idx in range(len(s1))])

def commonSeq(s1, s2):
    # return set of common letters (in original order)
    from functools import reduce
    return reduce(lambda acc, curr: acc + (curr[1] if (s1[curr[0]] == s2[curr[0]]) else ""), enumerate(s1), "")

# Compare all pairs of boxIDx for 1 dist pair O(n^2)
for idx1 in range(len(boxIds)):
    for idx2 in range(idx1+1, len(boxIds)):
        currDiff = diffDist(boxIds[idx1], boxIds[idx2])
        # Correct IDs (diff by 1 only) ---> print common letter
        if (currDiff == 1): print(commonSeq(boxIds[idx1], boxIds[idx2]))

