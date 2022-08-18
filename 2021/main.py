
import pathlib

# import each day files
import day1.day1 as d1
import day2.day2 as d2
import day3.day3 as d3

# import utils
import utils.utils as utils

# Main directory
mainDir = pathlib.Path(".")

print("######################")
print(pathlib.Path("."))
print(pathlib.Path.cwd())
print(mainDir)
print("######################")

# main entry
if __name__ == "__main__":
    print("Solving")
    # d1.solve(utils.readFile(mainDir / "day1/input.in"))
    # d2.solve(utils.readFile(mainDir / "day2/input.in"))
    d3.solve(utils.readFile(mainDir / "day3/input.in"))
