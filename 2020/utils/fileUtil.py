import os

# File utils

def readFile(file_path):
    file_contents = None
    with open(file_path, "r") as f:
        file_contents = f.readlines()
    return [l.strip() for l in file_contents]

