# read input
import re
from collections import defaultdict, namedtuple
Claim = namedtuple('Claim', ['left', 'top', 'w', 'h'])
with open('./1203.in', 'r') as f:
    # split tokens, regexp delimiter 3 diff markers, cast int, unpack for 'Claim' namedtuple
    claims = [Claim(*[int(x) for x in re.split(',|:|x', ''.join(l.split()[2:]))]) for l in f.readlines()]

# print(len(claims))
#####################################
# 1 - find slots that are overlapped by 2+ claims
#####################################

# Too expensive to test for each slot - instead count each claim slot occurrence

Pos = namedtuple('Pos', ['x', 'y'])
posOccurs = defaultdict(int)
for c in claims:
    # Flattened list (instead of normal 2D matrix --- only 1 set of square brackets)
    for p in [Pos(col, row) for row in range(c.top, c.top+c.h) for col in range(c.left, c.left+c.w)]:
        posOccurs[p] += 1

multOccurPos = [p for p, count in posOccurs.items() if count > 1]

# positions covered by ANY claims
# print(len(posOccurs))
# positions covered by 2+ claims
# print(len(multOccurPos))

#####################################
# 2 - Find 1 claim that does NOT overlap at all
#####################################

for idx, c in enumerate(claims):
    # overlap position in curr claim
    if any([((p.y in range(c.top, c.top+c.h)) and (p.x in range(c.left, c.left+c.w))) for p in multOccurPos]):
        continue
    print(idx+1, c)


