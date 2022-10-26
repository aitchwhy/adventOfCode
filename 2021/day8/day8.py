
def parseEntry(content):
    # parse input. (10 unique signal patterns | 4 output values)
    # print(f"parsing line {signals} and {output}")
    tokens = content.split(" ")

    # delimit by using token word. Use itertools.groupby (acts like Unix uniq)
    from itertools import groupby
    grouped = [list(lst) for k, lst in groupby(
        tokens, key=lambda x: x == "|") if (k is False)]

    entry = Entry(signals=grouped[0], output=grouped[1])
    # print(entry)
    return entry


class Entry:
    def __init__(self, signals, output) -> None:
        self.signals = signals
        self.output = output
        # maps jumbled digit->real digit int
        self.jumbleMap: dict[frozenset, int] = dict()

    # orig mapping : a,b,c,d,e,f,g - topleft to bottomright
    def solve(self):
        # identify unique numbers in jumbled.
        # 1,4,7,8 -> unique
        # 2,3,5,6,9,0 -> not unique
        # 2 - 5 segs. (of 2,5) - when subtract "4", 3 len left.
        # 3 - 5 segs. (of 2,3,5). When unioned with "1". no change.
        # 5 - 5 segs. (of 2,5) - when subtract "4", 2 len left.
        # 6 - 6 segs. (of 6,9,0) - when subtract "1" - 1 removed.
        # 9 - 6 segs. (of 9,0) - when subtract "4" - 4 removed.
        # 0 - 6 segs. (of 9,0) - when subtract "4" - 3 removed.
        # numToSig[num] = signal string
        numToSig = [None] * 10
        seg5 = []
        seg6 = []
        for s in self.signals:
            # 1,4,7,8 -> unique
            if len(s) == 2:  # 1
                self.jumbleMap[frozenset(s)] = 1
                numToSig[1] = s
            elif len(s) == 4:  # 4
                self.jumbleMap[frozenset(s)] = 4
                numToSig[4] = s
            elif len(s) == 3:  # 7
                self.jumbleMap[frozenset(s)] = 7
                numToSig[7] = s
            elif len(s) == 7:  # 8
                self.jumbleMap[frozenset(s)] = 8
                numToSig[8] = s
            elif len(s) == 5:  # 2,3,5
                seg5.append(s)
            elif len(s) == 6:  # 6,9,0
                seg6.append(s)

        # union with 1 (find 3)
        for s in seg5:
            beforeSLen = len(s)
            afterSLen = len(set(s) | set(numToSig[1]))
            if beforeSLen == afterSLen:
                self.jumbleMap[frozenset(s)] = 3
                numToSig[3] = s

        # sub 4 (differentiate 2,5)
        for s in [x for x in seg5 if x != numToSig[3]]:
            beforeSLen = len(s)
            afterSLen = len(set(s) - set(numToSig[4]))
            if (beforeSLen - afterSLen) == 3:
                self.jumbleMap[frozenset(s)] = 2
                numToSig[2] = s
            elif (beforeSLen - afterSLen) == 2:
                self.jumbleMap[frozenset(s)] = 5
                numToSig[5] = s

        # sub 1 (find 6)
        # 6 - 6 segs. (of 6,9,0) - when subtract "1" - only 1 removed.
        for s in seg6:
            beforeSLen = len(s)
            afterSLen = len(set(s) - set(numToSig[1]))
            if beforeSLen == (afterSLen+1):
                self.jumbleMap[frozenset(s)] = 6
                numToSig[6] = s

        # sub 1 (find 6) - 2 removed
        # 9 - 6 segs. (of 9,0) - when subtract "4" - 4 removed.
        # 0 - 6 segs. (of 9,0) - when subtract "4" - 3 removed.
        for s in [x for x in seg6 if x != numToSig[6]]:
            beforeSLen = len(s)
            afterSLen = len(set(s) - set(numToSig[4]))
            if (beforeSLen - afterSLen) == 3:
                self.jumbleMap[frozenset(s)] = 0
                numToSig[0] = s
            elif (beforeSLen - afterSLen) == 4:
                self.jumbleMap[frozenset(s)] = 9
                numToSig[9] = s

        # print(self.jumbleMap, seg5, seg6, numToSig)

        # TODO: when keyed output digit can be in DIFFERENT ORDER! make it ordered or use frozen set as key

        # return 4 digit output
        final = 0
        for o in self.output:
            final *= 10
            final += int(self.jumbleMap[frozenset(o)])
        return final

    def __repr__(self) -> str:
        return f"signals {self.signals} and output {self.output} with mapping {self.jumbleMap}"


def solve(lineContents):
    print("Day 8 solution")

    # parse input. (10 unique signal patterns | output values)
    entries = []
    it = iter(lineContents)
    while True:
        try:
            # Will raise StopIteration exception when no more lines
            entry = parseEntry(next(it))
            entries.append(entry)
        except StopIteration:
            break

    # print(entries)

    # part 1. Find in output how many times unique numbers (1,4,7,8) appear
    # count = 0
    # for entry in entries:
    #     for o in entry.output:
    #         if len(o) in [2, 4, 3, 7]:
    #             count += 1
    # print(count)

    # part 2. Decode all jumbled signals. Then sum all 4 digit numbers.
    for entry in entries:
        entry.solve()
        print(f"solved entry : {entry}")
        return
