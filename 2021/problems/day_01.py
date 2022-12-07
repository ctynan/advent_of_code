INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2021/inputs"
input_path = f"{INPUT_PREFIX}/day_01.txt"

### PART ONE
f_in = open(input_path)
tot = 0
cur = int(next(f_in))

while True:
    try:
        new_depth = int(next(f_in))
    except StopIteration:
        break
    if new_depth > cur:
        tot += 1
    cur = new_depth

print(tot)

### PART TWO
f_in = open(input_path)
tot = 0
first = int(next(f_in))
second = int(next(f_in))
third = int(next(f_in))

while True:
    try:
        new_depth = int(next(f_in))
    except StopIteration:
        break
    if new_depth > first:
        tot += 1
    first = second
    second = third
    third = new_depth

print(tot)