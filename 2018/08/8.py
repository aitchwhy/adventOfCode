###########################
# Imports
###########################
import fileinput


###########################
# Custom class
###########################
class Node(object):
    def __init__(self):
        self.children = []
        self.meta = []
    def __repr__(self):
        return "(meta : {})".format(self.meta)

###########################
# Read content (use 'fileinput' to get filename from CLI arg)
###########################
for line in fileinput.input():
    encodedTree = iter(line.split())


###########################
# Part 1 - Sum of all metadata entries
###########################

# Can't define boundaries for each 'child' prior to parsing them...
# so iterate content and create nodes over pass of content

metaSum = 0

def populateTree():
    # Base condition - (end of encoded content)
    numChildren = int(next(encodedTree, None))
    if (numChildren == None): return

    # 1 tree node handle
    n = Node()
    numMeta = int(next(encodedTree, None))

    # Create children
    for _ in range(numChildren):
        n.children.append(populateTree())

    # Finish creating current node
    for _ in range(numMeta):
        n.meta.append(int(next(encodedTree, None)))

    global metaSum
    metaSum += sum(n.meta)

    return n

root = populateTree()
print(metaSum)


###########################
# Part 2 - Find "value" of root node ("value" := sum(meta) if leafNode else sum(meta to 1-index children (skip if DNE))
###########################

def getValue(n):
    if (len(n.children) == 0): return sum(n.meta)
    return sum([getValue(n.children[cIdx-1]) for cIdx in n.meta if (1 <= cIdx <= len(n.children))])

print(getValue(root))
