
def calculateCost(alignedPos, positions, costFunc):
    return sum(map(lambda p: costFunc(p, alignedPos), positions))


def calculateMinCost(positions, costFunc):
    minPos, maxPos = min(positions), max(positions)
    minCost = float('inf')
    for pos in range(minPos, maxPos+1):
        cost = calculateCost(pos, positions, costFunc)
        minCost = min(minCost, cost)
        # print(f"pos: {pos}, cost: {cost}, with new minCost: {minCost}")
    return minCost


def solve(lineContents):
    print("Day 7 solution")
    # parse line as positions
    positions = [int(x) for x in lineContents[0].split(",")]
    # print(positions)

    # part 1 - find position that requires least movement for all positions.
    minCost = calculateMinCost(positions, lambda p, a: abs(p - a))
    print(f"part 1 mincost: {minCost}")
    # print(f"calculated cost for 2 : {calculateCost(2, positions)}")

    # part 2 - still find min cost position, but cost function is different.
    from itertools import count, islice
    minCost2 = calculateMinCost(
        positions,
        lambda p, a: sum(islice(
            count(start=1),
            0,
            abs(p-a),
        )),
    )
    print(f"part 2 mincost: {minCost2}")
