import os
INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2024/inputs"
input_path = f"{INPUT_PREFIX}/day_02.txt"

### PART ONE
def is_level_safe(x):
    # check if increasing or decreasing
    if x != sorted(x) and x != sorted(x, reverse=True):
        return False
    y = x[1:]
    for idx, _ in enumerate(y):
        if abs(y[idx]-x[idx]) == 0 or abs(y[idx]-x[idx]) > 3:
            return False
    
    return True

f_in = open(input_path)
tot = 0
for line in f_in.readlines():
    lvl = line.strip().split()
    lvl = list(map(int, lvl))
    tot += 1 if is_level_safe(lvl) else 0 

print(tot)

### PART TWO

f_in = open(input_path)
tot = 0
for line in f_in.readlines():
    lvl = line.strip().split()
    lvl = list(map(int, lvl))
    if is_level_safe(lvl):
        tot += 1
    else:
        for idx in range(len(lvl)):
            sub_lvl = lvl[:idx] + lvl[(idx+1):] 
            if is_level_safe(sub_lvl):
                tot += 1
                break

print(tot)

