import os
INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/problems/inputs"
input_path = f"{INPUT_PREFIX}/day_01_easy.txt"
f_in = open(input_path)

### PART ONE
best, cur = 0, 0

for line in f_in.readlines():
    if len(line.strip()) == 0:
        best = max(cur, best)
        cur = 0
    else:
        cur += int(line.strip())

print(best)

### PART TWO
f_in = open(input_path)
amounts, cur = [], 0
for line in f_in.readlines():
    if len(line.strip()) == 0:
        amounts.append(cur)
        cur = 0
    else:
        cur += int(line.strip())
if cur > 0:
    amounts.append(cur)

amounts = sorted(amounts, reverse=True)
print(sum(amounts[:3]), amounts[:3])