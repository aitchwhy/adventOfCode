
# Imports
from collections import namedtuple, deque, defaultdict
import heapq
import re

# String parsing -> named tuple
Req = namedtuple('Req', ['before', 'after'])
def parse(s):
    matches = re.match('Step (.) .* step (.)', s)
    return Req(matches.group(1), matches.group(2))

# Read input
with open('./1207.in', 'r') as f:
    reqs = [parse(l.strip()) for l in f.readlines()]

# Build matrix (adj. list)
m_in = defaultdict(list)
m_out = defaultdict(list)
for r in reqs:
    m_out[r.before].append(r.after)
    m_in[r.after].append(r.before)

###############################
# Visualization (Graphviz Digraph)
# --- CLI usage: dot -Txxx dotFile.dot -o graphName.xxx
###############################
with open('./1207.dot', 'w') as f:
    f.write("digraph {\n")
    f.write("rankdir=LR;")
    for k,v in m_out.items():
        # Double "{{" or "}}" to ESCAPE in format string
        f.write("{} -> {{{}}};\n".format(k,' '.join(v)))
    f.write("}\n")

########################################
# Part 1 - Print order satisfying requirements (topological sort)
########################################


# sort over (incoming edges count, key alphabet)
# list(m) ---> list-ified over (, key alphabet)
steps = deque([])
visited = set()
print("########### OUT #############")
print(*m_out.items(), sep='\n')

# Topological (break ties by alphabet) --- Kahn's algorithm
# Start with 0 outgoing-edge nodes
S = [n for n in m_out.keys() if (len(m_in[n]) == 0)]
print(S)
heapq.heapify(S)
while (len(S) > 0):
    # Pick 1 from set (break ties ALPHABETical) + add to TAIL
    node = heapq.heappop(S)
    steps.append(node)
    # For each edge INTO 'node' - remove edge + if no other incoming, insert source into 'S'
    for child in m_out[node].copy():
        # Remove edge (node -> child)
        m_out[node].remove(child)
        m_in[child].remove(node)
        # if no more incoming for child, add to set of 0 incoming 'S'
        if (len(m_in[child]) == 0):
            heapq.heappush(S, child)


# If graph has remaining edges -> cycle ELSE 'steps'
# GJFMDHNBCIVTUWEQYALSPXZORK --- correct
print(''.join(steps))

########################################
# Part 2 - parallel working schedule (construct & how long to complete?)
########################################

########################################
# Lessons
########################################

'''
(0) topological sort -> Kahn's Algorithm
- 
(1) Iterating dict keys --- Cannot call [for x in dict.keys()] in Python 3.x because "keys()" ---> returns ITERATOR...NOT...LIST
(2) String format --- Double "{{" or "}}" to ESCAPE in format string
(3) Sorting --- multiple keys ... return tuple (key = lambda x: (x[1], x[2]))
'''
