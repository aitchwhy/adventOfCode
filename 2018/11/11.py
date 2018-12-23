from collections import defaultdict
import fileinput

gridSerial = None
for l in fileinput.input():
    gridSerial = (int(l))

##################################
# Part 1 - find max power 3x3
##################################

print(gridSerial)
def power(x,y,serial):
    rackId = x + 10
    powerLevel = rackId * y
    powerLevel += serial
    powerLevel *= rackId
    powerLevel = 0 if (powerLevel < 100) else ((powerLevel // 100) % 10)
    powerLevel -= 5
    return powerLevel

assert(power(3,5,8) == 4)
assert(power(122,79,57) == -5)
assert(power(217,196,39) == 0)
assert(power(101,153,71) == 4)


# For each potential top-left out of 300,300 matrix, find 1 with MAX power
topLefts = [(x,y) for x in range(300-3+1) for y in range(300-3+1)]
maxTopLeft = max(topLefts, key=lambda p: sum([power(p[0]+dx, p[1]+dy, gridSerial) for dx in range(3) for dy in range(3)]))
print(maxTopLeft)

##################################
# Part 2 - find max power NxN
##################################

# Optimization -> "summed area table" : pre-calculate sums for each cell (top-left -> curr cell)
summed_area_table = defaultdict(int)
for x in range(1,301):
    for y in range(1,301):
        summed_area_table[(x,y)] = power(x,y,gridSerial) + \
                                    summed_area_table[(x-1,y)] + \
                                    summed_area_table[(x,y-1)] - \
                                    summed_area_table[(x-1,y-1)]

def calcRegionSum(topLeftX, topLeftY, bottomRightX, bottomRightY):
    return summed_area_table[(bottomRightX, bottomRightY)] - \
            summed_area_table[(bottomRightX, topLeftY-1)] - \
            summed_area_table[(topLeftX-1, bottomRightY)] + \
            summed_area_table[(topLeftX-1, topLeftY-1)]

maxTopLeft, maxDim, maxPower = None, None, float('-inf')
for dim in range(1,301):
    print(dim)
    for topLeft in [(x,y) for x in range(300-dim+1) for y in range(300-dim+1)]:
        currPower = calcRegionSum(topLeft[0], topLeft[1], topLeft[0]+dim-1, topLeft[1]+dim-1)
        if (currPower > maxPower):
            maxTopLeft, maxDim, maxPower = topLeft, dim, currPower

print(maxTopLeft, maxDim, maxPower)


