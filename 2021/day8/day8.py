
def parseEntry(content):
    # parse input. (10 unique signal patterns | output values)
    # print(f"parsing line {signals} and {output}")
    tokens = content.split(" ")

    # delimit by using token word. Use itertools.groupby (acts like Unix uniq)
    from itertools import groupby
    grouped = [list(lst) for k, lst in groupby(
        tokens, key=lambda x: x == "|") if (k is False)]
    # print(grouped)

    entry = Entry(signals=grouped[0], output=grouped[1])
    return entry


class Entry:
    def __init__(self, signals, output) -> None:
        self.signals = signals
        self.output = output

    def __repr__(self) -> str:
        return f"signals {self.signals} and output {self.output}"


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
    count = 0
    for entry in entries:
        for o in entry.output:
            if len(o) in [2, 4, 3, 7]:
                count += 1
    print(count)

    # part 1. Find in output

    # part 2.
