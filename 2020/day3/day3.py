# Day 2, 2020

def solve(input_lines):

    print(f"######### Day 3")

    # 1 down, 3 right
    colCount, rowCount = len(input_lines[0]), len(input_lines)
    
    # get input + parse into 2D matrix -> don't need to do since string can be indexed just the same way
    
    # util function for wrap around indexing
    def getTrueIndex(rowIdx, colIdx):
        return (rowIdx, (colIdx % colCount))

    print(f"raw input {(50, 50)} becomes {getTrueIndex(50, 50)}")

    # util function for isTree(x,y)
    TREE, LAND = "#", "."
    def isTree(rowIdx, colIdx):
        trueRowIdx, trueColIdx = getTrueIndex(rowIdx, colIdx)
        return input_lines[trueRowIdx][trueColIdx] == TREE

    # for x in range(colCount):
    #     print(f"{0, x} is tree : {isTree(0, x)}")

    # return count of trees
    treeCounter = 0
    rowIdx, colIdx = 0, 0
    for iterIdx in range(rowCount):
        # print(rowIdx, colIdx)
        treeCounter += (1 if isTree(rowIdx, colIdx) else 0)
        rowIdx, colIdx = rowIdx + 1, colIdx + 3
    # print(treeCounter)


    # part 2

    # slope := (row offset, col offset)
    slopes = [
        (1,1),
        (1,3),
        (1,5),
        (1,7),
        (2,1)
    ]
    acc = 1
    for s in slopes:
        treeCounter = 0
        rowIdx, colIdx = 0, 0
        for iterIdx in range(rowCount // s[0]):
            # print(f"Row-Col : {rowIdx}-{colIdx} ")
            treeCounter += (1 if isTree(rowIdx, colIdx) else 0)
            rowIdx, colIdx = rowIdx + s[0], colIdx + s[1]
        print(treeCounter)
        acc *= treeCounter

    print(acc)




# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.




