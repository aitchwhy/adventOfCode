
from collections import Counter

# day 3 solutions


def getMostCommonBitStr(binStrList):
    ctrs = [Counter() for _ in range(len(binStrList[0].strip()))]
    for binStr in binStrList:
        for idx, ch in enumerate(binStr.strip()):
            ctrs[idx][ch] += 1
    # Break tie by using "1"
    finalStr = ""
    for idx, ctr in enumerate(ctrs):
        mostCommon = ctr.most_common(1)[0]
        print(
            f"most common : {mostCommon} + len(binStrList) : {len(binStrList)}")
        if (mostCommon[1] == (len(binStrList) / 2)):
            finalStr += "1"
        else:
            finalStr += mostCommon[0]
    return finalStr
    # return "".join([ctr.most_common(1)[0][0] for ctr in ctrs])


def getLeastCommonBitStr(binStrList):
    return "".join([str(1 - int(ch)) for ch in getMostCommonBitStr(binStrList)])


def filterByCommonBit(candidatesBinStrList, commonBitStr, idx):
    return list(filter(lambda x: x[idx] == commonBitStr[idx], candidatesBinStrList))


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

    # filter using MOST common bits
    # commonStr = getMostCommonBitStr(lineContents)
    # leastCommonStr = getLeastCommonBitStr(lineContents)
    # print(f"commonStr : {commonStr} --- leastCommonStr : {leastCommonStr}")
    oxygenList = lineContents
    for idx in range(len(oxygenList[0].strip())):
        leastCommonStr = getMostCommonBitStr(oxygenList)
        print(f"common str : {leastCommonStr}")
        oxygenList = filterByCommonBit(
            oxygenList, leastCommonStr, idx,
        )
        print(f"oxygen list : {oxygenList}")
        if (len(oxygenList) == 1):
            break
    oxygen = binTodec("".join(oxygenList[0]))
    print(oxygen)

    # filter using LEAST common bits
    co2List = lineContents
    for idx in range(len(co2List[0].strip())):
        leastCommonStr = getLeastCommonBitStr(co2List)
        print(f"least common str : {leastCommonStr}")
        co2List = filterByCommonBit(
            co2List, leastCommonStr, idx,
        )
        print(f"co2 list : {co2List}")
        if (len(co2List) == 1):
            break
    co2 = binTodec("".join(co2List[0]))
    print(co2)

    # co2List = lineContents
    # for idx, commonCh in enumerate(epsilonBinStr):
    #     co2List = list(filter(lambda x: x[idx] == commonCh, co2List))
    #     if (len(co2List) == 1):
    #         break
    # print(f"NOT common str : {epsilonBinStr}")
    # print(f"co2 list : {co2List[0]}")
    # co2 = binTodec("".join(co2List[0]))

    lifeSupport = oxygen * co2

    print(f"life support : {lifeSupport}")
