##############
# Imports
##############
import re
from datetime import datetime
from collections import defaultdict, Counter

##############
# Classes
##############
# [1518-07-18 00:14] wakes up
class Record():
    def __init__(self, recStr):
        # Match pattern (escape square brackets)
        match = re.match(r"\[(.*)\] (.*)", recStr)
        tokens = [int(n) for n in re.split("-|:| ", match.group(1))]
        self.time = datetime(*tokens[:3], hour=tokens[3], minute=tokens[4])
        self.action = match.group(2)

    def __repr__(self):
        return "time : {} -- action : {}".format(self.time, self.action)

##############
# Read input
##############
with open("./1204.in", 'r') as f:
    records = [Record(l.strip()) for l in f.readlines()]

# Sort by time
records.sort(key=lambda x: x.time)
# print(*records[:3], sep='\n')

#########################################
# 1
# - Find guard with most minute asleep
# - what min does that guard sleep most?
#########################################

# Construct timeline (for each guard)
guardSleepMins = defaultdict(list)
guardNum = -1
for r in records:
    if ("asleep" in r.action):
        asleepTime = r.time.minute
    elif ("wakes" in r.action):
        # Record [asleep -> awake)
        for m in range(asleepTime, r.time.minute):
            guardSleepMins[guardNum].append(m)
    else:
        guardNum = int(re.search("#(\d+)", r.action)[1])

# print(*records[:5], sep='\n')
# print(guardSleepMins.keys(), sep='\n')
# print(len(guardSleepMins.values()))

# Guard with most sleep - 3167
sleepyGuardId = max(guardSleepMins.keys(), key=lambda g: len(guardSleepMins[g]))
print(sleepyGuardId)

# Minute with CHOSEN guard most sleeping - 45
print(Counter(guardSleepMins[sleepyGuardId]).most_common(1)[0])

#########################################
# 2 - Find 1 guard most frequently asleep on same minute
#########################################

# Compare & find max num slept by guard on their max min
maxSlept = None
for g, sleepingMins in guardSleepMins.items():
    currGuardMaxSlept = Counter(sleepingMins).most_common(1)[0]
    if ((maxSlept == None) or
            (maxSlept[1][1] < currGuardMaxSlept[1])):
        maxSlept = (g, currGuardMaxSlept)

# Guard 179 - min 30
print(maxSlept)
print(maxSlept[0] * maxSlept[1][0])




###########################################################
# Lessons
###########################################################

'''
(0) 'print' pretty multiline

    - print(*iter, sep='\n') : unpacked iter (as if passed in each with comma, will be printed with separating char space by default... but i can change that to be NEWLINE) --- Useful for formatting (2D arrays)

(1) 're' library (used to find groups! extracting info from input)

    - re.split : Splits on delimiters separated by '|'
    - re.match : searches from STRING beginning
    - re.search : searches from start
    - (matchObj).group(0) or (matchObj)[0] : FULL match, 1,2, are indexed groups

(2) 'datetime' library

    - Create time object

(3) 'collections.Counter' library

    - Counting objects (hashable)
    - Init from ITER / dict mapping / keyword args
    - Can find most common using 'Counter.most_common(1)'

'''

