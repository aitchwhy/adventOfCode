
# file util functions


def readFile(filePath):
    fileContents = None
    with open(filePath, "r") as f:
        fileContents = [x.strip() for x in f.readlines()]
    return fileContents
