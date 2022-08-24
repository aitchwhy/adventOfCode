
# TODO: create class for board
class Board():
    def __init__(self, boardlines):
        self.N = len(boardlines)
        self.boardlines = boardlines
        self.boardcalled = [[False] * self.N for _ in range(self.N)]
        self.lastCalled = None

    def addNum(self, num):
        # check number if exists + update
        for i in range(self.N):
            for j in range(self.N):
                if self.boardlines[i][j] == num:
                    self.boardcalled[i][j] = True

        # Update last called number
        self.lastCalled = num

    # returns (isBingo, isRow, bingoIdx)
    def hasBingo(self):
        for i in range(self.N):
            # row bingo
            if all(self.boardcalled[i]):
                return (True, True, i)
            # columns bingo
            if all([self.boardcalled[j][i] for j in range(self.N)]):
                return (True, False, i)
        return (False, None, None)

    def getLastCalled(self):
        return self.lastCalled

    def getUncalledSum(self):
        uncalledSum = 0
        for i in range(self.N):
            for j in range(self.N):
                if not self.boardcalled[i][j]:
                    uncalledSum += self.boardlines[i][j]
        return uncalledSum

    def __repr__(self):
        finalStr = "\n"
        for i, numList in enumerate(self.boardlines):
            for j, num in enumerate(numList):
                finalStr += f"{str(num)}[{self.boardcalled[i][j]}]" + " "
            finalStr += "\n"
        return finalStr


def solve(inputLines):
    print("hello")
    print(inputLines)
    linesIter = iter(inputLines)

    # parse number sequence
    numSeqStr = next(linesIter)
    numSeq = [int(x) for x in numSeqStr.strip().split(",")]
    print(f"number sequence : {numSeq}")

    # TODO: parse boards
    boards = []
    while (True):
        blankLine = next(linesIter, None)
        if (blankLine is None):
            break
        boardLines = []
        for _ in range(5):
            boardLine = [int(x) for x in (next(linesIter).strip().split())]
            boardLines.append(boardLine)
        boards.append(Board(boardLines))

    # part 1

    # for n in numSeq:
    #     for b in boards:
    #         b.addNum(n)
    #         bingoInfo = b.hasBingo()
    #         if bingoInfo[0]:
    #             print(f"bingo with winning board : {b}")
    #             print(f"winning board info : {bingoInfo}")
    #             lastCalled = b.getLastCalled()
    #             uncalledSum = b.getUncalledSum()
    #             print(f"last called : {lastCalled}")
    #             print(f"final number : {lastCalled * uncalledSum}")
    #             break
    #             # return b.getLastCalled()

    # part 2
    unfinishedBoards = len(boards)
    for n in numSeq:
        for b in boards:
            if b.hasBingo()[0]:
                continue
            b.addNum(n)
            bingoInfo = b.hasBingo()
            if bingoInfo[0]:
                print(f" ############ unfinished count : {unfinishedBoards}")
                if (unfinishedBoards == 1):
                    print(f"bingo with last winning board : {b}")
                    print(f"winning board info : {bingoInfo}")
                    lastCalled = b.getLastCalled()
                    uncalledSum = b.getUncalledSum()
                    print(f"last called : {lastCalled}")
                    print(f"final number : {lastCalled * uncalledSum}")
                    return
                unfinishedBoards -= 1
