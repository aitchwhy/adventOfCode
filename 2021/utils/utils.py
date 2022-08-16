
# file util functions


def readFile(filePath):
    fileContents = None
    with open(filePath, "r") as f:
        fileContents = f.readlines()
    return fileContents
