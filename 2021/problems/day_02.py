INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2021/inputs"
input_path = f"{INPUT_PREFIX}/day_02.txt"

### PART ONE
f_in = open(input_path)
length, depth = 0, 0

while True:
    try:
        instruction = next(f_in)
    except StopIteration:
        break
    if instruction.startswith("forward"):
        length += int(instruction.split()[-1])
    elif instruction.startswith("up"):
        depth -= int(instruction.split()[-1])
    elif instruction.startswith("down"):
        depth += int(instruction.split()[-1])
    else:
        raise Exception

print(length*depth)

### PART TW0
f_in = open(input_path)
aim, length, depth = 0, 0, 0

while True:
    try:
        instruction = next(f_in)
    except StopIteration:
        break
    if instruction.startswith("forward"):
        length += int(instruction.split()[-1])
        depth += int(instruction.split()[-1])*aim
    elif instruction.startswith("up"):
        aim -= int(instruction.split()[-1])
    elif instruction.startswith("down"):
        aim += int(instruction.split()[-1])
    else:
        raise Exception

print(length*depth)