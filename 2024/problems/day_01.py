import os
INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2024/inputs"
input_path = f"{INPUT_PREFIX}/day_01.txt"

### PART ONE
f_in = open(input_path)
x, y = [], []

for line in f_in.readlines():
    a, b = line.strip().split()
    x.append(int(a))
    y.append(int(b))

x, y = sorted(x), sorted(y)
tot = sum([abs(x[i]-y[i]) for i in range(len(x))])

print(tot)

### PART TWO
tot = 0
for _, v in enumerate(x):
    repeats = [z for z in y if z == v]
    tot += v * len(repeats)

print(tot)