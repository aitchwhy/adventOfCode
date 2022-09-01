
def calculateCost(alignedPos, positions):
    return sum(map(lambda p: abs(p - alignedPos), positions))


def calculateMinCost(positions):
    minPos, maxPos = min(positions), max(positions)
    minCost = float('inf')
    for pos in range(minPos, maxPos+1):
        cost = calculateCost(pos, positions)
        minCost = min(minCost, cost)
        # print(f"pos: {pos}, cost: {cost}, with new minCost: {minCost}")
    return minCost


def solve(lineContents):
    print("Day 7 solution")
    # parse line as positions
    positions = [int(x) for x in lineContents[0].split(",")]
    # print(positions)

    # part 1 - find position that requires least movement for all positions.
    minCost = calculateMinCost(positions)
    print(f"mincost: {minCost}")
    # print(f"calculated cost for 2 : {calculateCost(2, positions)}")
