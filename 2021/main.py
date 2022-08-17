
import pathlib

# import each day files
import day1.day1 as d1
import day2.day2 as d2

# import utils
import utils.utils as utils

# Main directory
mainDir = pathlib.Path(".") / "2021"

print(pathlib.Path("."))
print(mainDir)

# main entry
if __name__ == "__main__":
    print("Solving")
    # d1.solve(utils.readFile("./day1/input.in"))
    d2.solve(utils.readFile("./day2/input.in"))
