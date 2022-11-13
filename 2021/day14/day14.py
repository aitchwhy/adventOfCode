

class Rule():
    def __init__(self, before, after) -> None:
        self.before = before
        self.after = after

    # def __repr__(self) -> str:
    #     return f"({self.before}) -> ({self.after})"

    # # Make this hashable in dictionary. Assume good input (self.before unique)
    # def __hash__(self):
    #     return hash(self.before)

    # def __eq__(self, otherRule):
    #     if not isinstance(otherRule, Rule):
    #         return False
    #     return (self.before == otherRule.Before)


class Polymer():
    SPLIT_STR = "->"

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
                             for x in l.split(Polymer.SPLIT_STR)]))
        return template, rules

    def __init__(self, template, rules) -> None:
        # part 1 init (naive full storage)
        self.template = template
        from collections import defaultdict
        self.rules = defaultdict(str)
        for r in rules:
            self.rules[r.before] = r.after

        # part 2 init. Counter(char), Counter(special pairs)
        from collections import Counter
        self.charCounts = Counter(self.template)
        from itertools import islice
        befores = islice(self.template, 0, len(self.template) - 1)
        afters = islice(self.template, 1, len(self.template))
        self.pairCounts = Counter([b+a for b, a in zip(befores, afters)])

    def __repr__(self) -> str:
        finalStr = "##############\n"
        finalStr += f"Char Counts : ({self.charCounts})\n"
        finalStr += "##############\n"
        finalStr += f"Pair Counts : ({self.pairCounts})\n"
        finalStr += "##############\n"
        finalStr += f"Template : ({self.template})\n"
        finalStr += "##############\n"
        finalStr += "Rules\n"
        print(self.rules)
        for before, after in self.rules.items():
            finalStr += f"{before}->{after}\n"
        finalStr += "##############"
        return finalStr

    def getMatched(self, matchStr):
        '''
        Return matched string (self.after) if arg string matches a rule.before.
        Return empty string if NO matches.
        '''
        return self.rules.get(matchStr, "")

    def turn(self) -> None:
        from itertools import zip_longest, islice, starmap, accumulate
        # generate pairs (consec 2 elems in order) for insertion computation.
        befores = islice(self.template, 0, len(self.template)-1)
        afters = islice(self.template, 1, len(self.template))
        templatePairs = ["".join(p) for p in zip_longest(befores, afters)]

        zipped = list(zip_longest(self.template, templatePairs))

        def ruleApplied(currChar, ruleMatchPair):
            # last char in template doesn't have pairs
            if (ruleMatchPair is None):
                return currChar
            if (ruleMatchPair in self.rules.keys()):
                return (currChar + self.rules[ruleMatchPair])
            return currChar

        rulesInserted = list(starmap(ruleApplied, zipped))

        # zip orig + inserted to flat array.
        accRulesInserted = list(accumulate(rulesInserted))[-1]

        # Update after turn
        self.template = (accRulesInserted)

    def optimizedTurn(self):
        # Keep counts only for reduced memory usage.
        # 1 turn -> update pair counts + update elem counts according to rules.
        for pair, count in list(self.pairCounts.items()):
            if (pair in self.rules):
                newChar = self.rules.get(pair, "")
                self.charCounts[newChar] += count
                newPair1, newPair2 = (pair[0] + newChar), (newChar + pair[1])
                self.pairCounts[pair] -= count
                if (newPair1 in self.rules):
                    self.pairCounts[newPair1] += count
                if (newPair2 in self.rules):
                    self.pairCounts[newPair2] += count


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

    # part 1. After 10 steps, find MOST + LEAST common element of final string.
    # - What is (MOST - LEAST) ?

    print(p)
    STEP_COUNT = 40
    for idx in range(STEP_COUNT):
        print(f"step : {idx}")
        # p.turn()
        p.optimizedTurn()

    # Python colletions.Counter can give MOST common -> LEAST (if no arg for num of most common elems specified)
    # from collections import Counter
    # cnt = Counter(p.template).most_common()
    # most_common, least_common = cnt[0], cnt[-1]
    # print(f"most common : {most_common}")
    # print(f"least common : {least_common}")
    # print(f"most - least diff : {most_common[1] - least_common[1]}")

    # part 2. Make 40 turns instead of 10 to get most-least.
    # TODO: times out if keeping full "template string" in memory. Optimize : keep dictionary of combos counts.
    cnt = (p.charCounts.most_common())
    most_common, least_common = cnt[0], cnt[-1]
    print(f"most common : {most_common}")
    print(f"least common : {least_common}")
    print(f"most - least diff : {most_common[1] - least_common[1]}")
