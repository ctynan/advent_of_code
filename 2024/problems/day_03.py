import os
import re
INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2024/inputs"
input_path = f"{INPUT_PREFIX}/day_03.txt"

### PART ONE

f_in = open(input_path)
tot = 0
for line in f_in.readlines():
    line = line.strip()
    res = re.findall(r"mul\(\d+,\d+\)", line)
    for v in res:
        v = v.replace('mul(', '').replace(')', '')
        v = v.split(',')
        v = list(map(int,v))
        tot += v[0] * v[1]

print(tot)

### PART TWO

f_in = open(input_path)
tot, enabled = 0, 1
for line in f_in.readlines():
    line = line.strip()
    res = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", line)
    for v in res:
        if v == "do()":
            enabled = 1
        elif v == "don't()":
            enabled = 0
        else:
            v = v.replace('mul(', '').replace(')', '')
            v = v.split(',')
            v = list(map(int,v))
            tot += v[0] * v[1] * enabled

print(tot)

