
import pathlib

# import each day files
import day1.day1 as d1
import day2.day2 as d2
import day3.day3 as d3
import day4.day4 as d4
import day5.day5 as d5
import day6.day6 as d6
import day7.day7 as d7
import day8.day8 as d8
import day9.day9 as d9
import day10.day10 as d10
import day11.day11 as d11
import day12.day12 as d12
import day13.day13 as d13
import day14.day14 as d14

# import utils
import utils.utils as utils

# Main directory
# mainDir = pathlib.Path(".")
mainDir = pathlib.Path(__file__).parent

print("######################")
# print(pathlib.Path("."))
# print(pathlib.Path.cwd())
# print(mainDir)
print("######################")

# main entry
if __name__ == "__main__":
    print("Solving")
    # d1.solve(utils.readFile(mainDir / "day1/input.in"))
    # d2.solve(utils.readFile(mainDir / "day2/input.in"))
    # d3.solve(utils.readFile(mainDir / "day3/input.in"))
    # d4.solve(utils.readFile(mainDir / "day4/input.in"))
    # d5.solve(utils.readFile(mainDir / "day5/input.in"))
    # d6.solve(utils.readFile(mainDir / "day6/input.in"))
    # d7.solve(utils.readFile(mainDir / "day7/input.in"))
    # d8.solve(utils.readFile(mainDir / "day8/input.in"))
    # d9.solve(utils.readFile(mainDir / "day9/input.in"))
    # d10.solve(utils.readFile(mainDir / "day10/input.in"))
    # d11.solve(utils.readFile(mainDir / "day11/input.in"))
    # d12.solve(utils.readFile(mainDir / "day12/input.in"))
    # d13.solve(utils.readFile(mainDir / "day13/input.in"))
    # d14.solve(utils.readFile(mainDir / "day14/sample.in"))
    d14.solve(utils.readFile(mainDir / "day14/input.in"))
