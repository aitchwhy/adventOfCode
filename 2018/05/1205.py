
from collections import deque
# Read input (polymer)
with open('./1205.in', 'r') as f:
    polymer = deque(f.read().strip())

# type : letter
# polarity : capitalization

###################################
# 1 - How many units remain after polymer reacts ?
###################################

# Adjacent : Same type & diff polarity DESTROYs
# Maintain stack of "reacted" - check top 2 

def destroy(c1, c2):
    # return (c1.lower() == c2.lower()) and (c1 != c2)
    return abs(ord(c1) - ord(c2)) == abs(ord('a') - ord('A'))

def reactPoly(polymer):
    reacted = deque()
    while (len(polymer) > 0):
        # reacted <--- polymer (1 at a time)
        reacted.append(polymer.popleft())
        # 'destroy' all possible top 2
        while ((len(reacted) >= 2) and (destroy(reacted[-1], reacted[-2]))):
            reacted.pop()
            reacted.pop()
    return reacted

# 11042
print(len(reactPoly(polymer.copy())))

###################################
# 2 - Find 1 unit whose removal gives best compression
###################################

minLen = float('inf')
for troubleMaker in range(ord('a'), ord('z')+1):
    # Pass in replaced COPY with lower,upper chars for this iter removed
    newLen = len(reactPoly(deque([e for e in polymer if (e not in [chr(troubleMaker), chr(troubleMaker).upper()])])))
    minLen = min(minLen, newLen)

# 10678 - too high
print(minLen)



###################################
# Lessons
###################################

'''
(1) Used 'deque' Library (efficient stack / queue)
(2) ALWAYS STRIP NEWLINE!!! (Caused off by 1 error)
(3) Create copies of Iterables if you're consuming it --- and you need new instances of it later on
'''

