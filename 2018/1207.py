
# Imports
from collections import namedtuple, deque, defaultdict, Counter
import heapq
import re
from itertools import count

# String parsing -> named tuple
Req = namedtuple('Req', ['before', 'after'])
def parse(s):
    matches = re.match('Step (.) .* step (.)', s)
    return Req(matches.group(1), matches.group(2))

# Read input
with open('./1207.in', 'r') as f:
    reqs = [parse(l.strip()) for l in f.readlines()]

# Build matrix (adj. list)
m_in, m_in_2 = defaultdict(list), defaultdict(list)
m_out, m_out_2 = defaultdict(list),defaultdict(list)
for r in reqs:
    m_out[r.before].append(r.after)
    m_out_2[r.before].append(r.after)
    m_in[r.after].append(r.before)
    m_in_2[r.after].append(r.before)

###############################
# Visualization (Graphviz Digraph)
# --- CLI usage: dot -Txxx dotFile.dot -o graphName.xxx
###############################
with open('./1207.dot', 'w') as f:
    f.write("digraph {\n")
    f.write("rankdir=LR;")
    f.write("graph [ordering=\"out\"];")
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

def writeWorking():
    with open('./temp.txt', 'w') as f:
        for w in workingSchedule:
            f.write(' '.join([(x if (x != None) else '.') for x in w]) + '\n')


numWorkers = 5

def workTime(s): return 60 + int(ord(s) - ord('A') + 1)

workingSchedule = [[] for _ in range(numWorkers)]

todos = Counter({ch : workTime(ch) for ch in ''.join(steps)})
print("TODOS : {}".format(todos))

zero_incoming = [n for n in m_out_2.keys() if (len(m_in_2[n]) == 0)]
heapq.heapify(zero_incoming)
totalTime = 0
finished = []

# Updates 'zero_incoming' to hold currently working projects
# (guaranteed topological sorted order, breaking ties alphabetically)
def updateWorkable():
    assert(len(zero_incoming) > 0)
    # Curr
    curr = heapq.heappop(zero_incoming)
    for child in m_out_2[curr].copy():
        # remove edge
        m_out_2[curr].remove(child)
        m_in_2[child].remove(curr)
        # Add child to zero-incoming if no incoming
        if (len(m_in_2[child]) == 0):
            heapq.heappush(zero_incoming, child)

    print("UPDATED zero_incoming : {}".format(zero_incoming))

# Work
for t in count():
    # Each prev worked accounted
    if (t > 0):
        todos -= Counter([w[-1] for w in workingSchedule if w[-1] != None])

    # Each worker curr work assignments
    for worker in workingSchedule:
        prevWork = None if (t == 0) else worker[-1]
        currWorking = [w[-1] for w in workingSchedule if len(w) > 0]

        # no prev work -> Get from (workable - curr working other workers)
        # prev work not finished -> continue working
        # prev work finished -> update workable to new

        # Update workables <--- prevWork & count == 0
        if ((prevWork != None) and (todos[prevWork] == 0)):
            finished.append(prevWork)
            updateWorkable()
        
        canWork = [n for n in zero_incoming if ((n not in finished) and (n not in currWorking))]

        # New work or Old work or None
        if ((prevWork != None) and (todos[prevWork] > 0)):
            # Unfinished work -> continue
            worker.append(prevWork)
        else:
            # print("@@@@@@@@@@@@@@@@@@@@@")
            # print("prev Work : {}".format(prevWork))
            # print("curr working : {}".format(currWorking))
            # print("zero_incoming : {}".format(zero_incoming))
            # print("canWork : {}".format(canWork))

            # None or finished work
            worker.append(sorted(canWork)[0] if (len(canWork) > 0) else None)

            # print("@@@@@@@@@@@@@@@@@@@@@")
            # print("prev Work : {}".format(prevWork))
            # print("curr working : {}".format(currWorking))
            # print("zero_incoming : {}".format(zero_incoming))
            # print("canWork : {}".format(canWork))
            # if (t > 100):
            #     writeWorking()
            #     exit()

    # Finish condition
    if (sum(todos.values()) == 0): break
    # print(len(zero_incoming))
    # print("sum(TODO) : {}".format(sum(todos.values())))
    totalTime += 1


writeWorking()
print(finished)
# 1183 --- too high
print(totalTime)



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
