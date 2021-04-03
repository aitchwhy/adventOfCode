# main entry Python class

# Day 1
import sys
import day1.day1 as d1
import utils.fileUtil
import pathlib

input_path_2020 = pathlib.Path(".") / "2020"
input_path_2020_day1 = input_path_2020 / "day1" / "input.in"

d1.solve(utils.fileUtil.readFile(input_path_2020_day1))
