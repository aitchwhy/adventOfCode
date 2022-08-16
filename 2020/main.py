# main entry Python class

# Day 1
import sys
import day1.day1 as d1
import day2.day2 as d2
import day3.day3 as d3
import day4.day4 as d4
import utils.fileUtil
import pathlib

input_path_2020 = pathlib.Path(".") / "2020"
# input_path_2020_day1 = input_path_2020 / "day1" / "input.in"
# input_path_2020_day2 = input_path_2020 / "day2" / "input.in"
# input_path_2020_day3 = input_path_2020 / "day3" / "input.in"
input_path_2020_day4 = input_path_2020 / "day4" / "input.in"

# d1.solve(utils.fileUtil.readFile(input_path_2020_day1))
# d2.solve(utils.fileUtil.readFile(input_path_2020_day2))
# d3.solve(utils.fileUtil.readFile(input_path_2020_day3))
d4.solve(utils.fileUtil.readFile(input_path_2020_day4))

