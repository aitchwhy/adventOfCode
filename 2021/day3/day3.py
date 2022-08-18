
from collections import Counter

# day 3 solutions


def binTodec(binStr):
    return int(binStr, 2)


def solve(lineContents):
    print("Hello world day 3")
    #####################
    # part 1.
    #####################

    # parse inputs - find counts of each column bits.
    # Each counters[i] is a counter for the ith column.
    counters = [Counter() for _ in range(len(lineContents[0].strip()))]
    for line in lineContents:
        for i, c in enumerate(line.strip()):
            counters[i][c] += 1
        # break

    # gamma rate binary bits (most common)
    gammaBinStr = [ctr.most_common(1)[0][0] for ctr in counters]
    print(gammaBinStr)
    gammaRate = binTodec("".join(gammaBinStr))

    # epsilon rate binary bits (most common)
    epsilonBinStr = [str(1 - int(ctr.most_common(1)[0][0]))
                     for ctr in counters]
    print(epsilonBinStr)
    epsilonRate = binTodec("".join(epsilonBinStr))

    # power = gamma rate * epsilon rate
    power = gammaRate * epsilonRate
    print(f"power : {power}")

    #####################
    # part 2.
    #####################

    pass
