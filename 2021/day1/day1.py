
# Find how many days Nth day increased compared to prev day.
# Note: 1st day does not count.

# 199, 200, 208, 210, 200 -> 3 times increased

def solve(inputLines):
    print("Day 1")

    # parse each line into integer
    inputInts = [int(line) for line in inputLines]

    # Part 1
    incCounter = 0
    for idx, depth in enumerate(inputInts):
        if idx == 0:
            continue
        if inputInts[idx] > inputInts[idx - 1]:
            incCounter += 1

    print(f"Day 1 Part 1 Solution: {incCounter}")

    # Part 2
    width = 3
    prevWindow = float('inf')
    windowIncCounter = 0
    for idx in range(len(inputInts) - width + 1):
        currWindow = sum(inputInts[idx:idx + width])
        print(prevWindow, currWindow)
        if prevWindow < currWindow:
            windowIncCounter += 1
        prevWindow = currWindow

    print(f"Day 1 Part 2 Solution: {windowIncCounter}")
