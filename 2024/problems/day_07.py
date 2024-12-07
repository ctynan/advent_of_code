INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2024/inputs"
input_path = f"{INPUT_PREFIX}/day_07.txt"

f_in = open(input_path)
inps = []
results = []

for line in f_in.readlines():
    line = line.strip()
    lv = line.split(':')
    results.append(int(lv[0]))
    inps.append(list(map(int,lv[1].strip().split())))

### PART ONE

def evaluate(running_total, inputs, operands):
    if len(inputs) == 0:
        return running_total

    val, operand = inputs.pop(0), operands.pop(0)

    if operand == '+':
        return evaluate(running_total + val, inputs, operands)
    if operand == '*':
        return evaluate(running_total * val, inputs, operands)
    if operand == '|':
        new_running_total = int(str(running_total) + str(val))
        return evaluate(new_running_total, inputs, operands)
    return -1

import itertools
tot = 0

for idx, v in enumerate(inps):
    tgt = results[idx]
    N = len(v)
    lst = map(list, itertools.product(['+', '*'], repeat=N-1))
    
    for operands in lst:
        if evaluate(v[0], v[1:], operands) == tgt:
            tot += tgt
            break

print(tot)

### PART TWO
tot = 0

for idx, v in enumerate(inps):
    tgt = results[idx]
    N = len(v)
    lst = map(list, itertools.product(['+', '*', '|'], repeat=N-1))
    
    for operands in lst:
        if evaluate(v[0], v[1:], operands) == tgt:
            tot += tgt
            break

print(tot)
