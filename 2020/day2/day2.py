# Day 2, 2020

def solve(input_lines):

    print(f"######### Day 2")
    
    from collections import namedtuple, Counter
    Range = namedtuple('range', ['start', 'end'])
    LineInfo = namedtuple('lineInfo', ['range', 'letter', 'pw'])

    # read / parse input
    def parseRange(rangeStr):
        startNum, endNum = rangeStr.split("-")
        return Range(int(startNum), int(endNum))
        return 

    def parseLetter(letterStr):
        return letterStr[:-1]

    def parsePassword(parsePassword):
        return parsePassword


    def parse(lineStr):
        tokens = lineStr.split(" ")
        rangeObj = parseRange(tokens[0])
        letterObj = parseLetter(tokens[1])
        passwordObj = parsePassword(tokens[2])
        return LineInfo(rangeObj, letterObj, passwordObj)


    inputInfos = [ parse(l) for l in input_lines ]

    # Find invalid password part 1
    def isValidOne(lineInfo):
        pwCounter = Counter(lineInfo.pw)
        letterCount = pwCounter[lineInfo.letter]
        return (lineInfo.range.start <= letterCount <= lineInfo.range.end)

    # Find invalid password part 2
    def isValidTwo(lineInfo):
        # Note : start, end are 1-indexed
        letter = lineInfo.letter
        idx1 = lineInfo.range.start
        idx2 = lineInfo.range.end
        # exactly 1 must be that letter
        idx1IsLetter = (lineInfo.pw[idx1-1] == letter)
        idx2IsLetter = (lineInfo.pw[idx2-1] == letter)
        return (idx1IsLetter) != (idx2IsLetter)

    #x = inputInfos[0]
    #y = isValid(inputInfos[0])
    #print(f"{x} --- {y}")


    # TODO: find count of invalids
    print(f"Total valids count : {len([x for x in inputInfos if isValidOne(x)])}")
    print(f"Total valids count : {len([x for x in inputInfos if isValidTwo(x)])}")
