
parenMap = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

ptMap = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


class Line:
    INCOMPLETE, COMPLETE = -1, 0

    def __init__(self, lineStr):
        self.line = lineStr

    def __repr__(self) -> str:
        return f"Line : {self.line}"

    def matchParens(self) -> int:
        '''
        Find the first incorrect character in the line
        Return the score of incorrect character
        '''
        stack = []
        for i, c in enumerate(self.line):
            # remember opened parens
            if c in parenMap:
                stack.append(c)
            else:
                # process closed parens
                if len(stack) == 0:
                    # no opened parens to match
                    return ptMap[c]
                else:
                    # check latest opened paren
                    if parenMap[stack[-1]] == c:
                        stack.pop()
                    else:
                        # incorrect paren
                        return ptMap[c]
        # no incorrect paren found
        # if incomplete -> return -1
        # if complete -> return 0
        return (Line.INCOMPLETE if len(stack) > 0 else Line.COMPLETE)


def solve(lineContents):
    print(f"solving day 10")

    # Each "chunk" is a valid parenthesis expression.
    # valid : (), [], {}, <>
    # lines are "corrupted" or "incomplete"
    # - corrupted : closes with wrong paren
    # - incomplete : no wrong parens (just some are left unclosed)

    # part 1. Find all corrupted lines and chars.
    # for each corrupted - find 1st incorrect char and score
    # ) : 3 pts
    # ] : 57 pts
    # } : 1197 pts
    # > : 25137 pts

    lines = []
    for l in lineContents:
        lines.append(Line(l))

    scoredLines = [l.matchParens() for l in lines]

    # print(*lines, sep='\n')
    # print(*scoredLines, sep='\n')
    print(f"sum of scored lines : {sum([s for s in scoredLines if s > 0])}")
