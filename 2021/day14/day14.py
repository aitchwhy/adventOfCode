

class Rule():
    SPLIT_STR = "->"

    def __init__(self, before, after) -> None:
        self.before = before
        self.after = after

    def __repr__(self) -> str:
        return f"({self.before}) -> ({self.after})"


class Polymer():

    @staticmethod
    def parseInput(lines):
        # template on line 0.
        # insertion rules line 2+.
        template, rules = None, []
        for idx, l in enumerate(lines):
            if (idx == 0):
                template = l
            elif (idx == 1) and (l == ""):
                continue
            else:  # idx >= 2
                rules.append(Rule(*[x.strip()
                             for x in l.split(Rule.SPLIT_STR)]))
        return template, rules

    def __init__(self, template, rules) -> None:
        self.template = template
        self.rules = rules

    def __repr__(self) -> str:
        finalStr = "##############\n"
        finalStr += f"Template : ({self.template})\n"
        finalStr += "##############\n"
        finalStr += "Rules\n"
        for r in self.rules:
            finalStr += f"{r}\n"
        finalStr += "##############"
        return finalStr


def solve(lineContents):
    # parse input.
    #
    # - polymer template (line 0)
    #   - starting point for polyer string.
    # - pair of insertion rules (line 2+).
    #   - XY -> Z : insert "Z" between "X" and "Y".
    #   - insertion "simultaneous" -> current turn insertion not considered for other insertions.
    template, rules = Polymer.parseInput(lineContents)
    p = Polymer(template, rules)

    print(p)

    # part 1. After 10 steps, find MOST + LEAST common element of final string.
    # - What is (MOST - LEAST) ?

    # part 2.
    pass
