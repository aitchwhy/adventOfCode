import pathlib
import utils

import day1.main as d1

mainDir = pathlib.Path(__file__).parent


# main entry point for all 2019 solutions
if __name__ == "__main__":
    print("Solving")
    d1.solve(utils.readFile(mainDir / "day1/input.in"))
