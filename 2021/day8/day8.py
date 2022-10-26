
def parseEntry(content):
    # parse input. (10 unique signal patterns | 4 output values)
    # print(f"parsing line {signals} and {output}")
    tokens = content.split(" ")

    # delimit by using token word. Use itertools.groupby (acts like Unix uniq)
    from itertools import groupby
    grouped = [list(lst) for k, lst in groupby(
        tokens, key=lambda x: x == "|") if (k is False)]

    entry = Entry(signals=grouped[0], output=grouped[1])
    print(entry)
    return entry


class Entry:
    def __init__(self, signals, output) -> None:
        self.signals = signals
        self.output = output
        # maps jumbled->output
        self.jumbleMap: dict[str, str] = dict()

    # orig mapping : a,b,c,d,e,f,g - topleft to bottomright
    def solve(self):
        # identify unique numbers in jumbled.
        # 1,4,7,8 -> unique
        # 2,3,5,6,9,0 -> not unique
        # 2 - 5 segs. (of 2,5) - when subtract "4", 3 len left.
        # 3 - 5 segs. (of 2,3,5). When unioned with "1". no change.
        # 5 - 5 segs. (of 2,5) - when subtract "4", 2 len left.
        # 6 - 6 segs. (of 6,9,0) - when subtract "1" - only 1 removed.
        # 9 - 6 segs. (of 6,9) - when subtract "4" - 3 removed.
        # 0 - 6 segs. (of 6,9) - when subtract "4" - 4 removed.
        pass

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
    count = 0
    for entry in entries:
        for o in entry.output:
            if len(o) in [2, 4, 3, 7]:
                count += 1
    print(count)

    # part 2. Decode all jumbled signals. Then sum all 4 digit numbers.
    for entry in entries:
        entry.solve()
        print(f"solved entry : {entry}")
