INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2022/inputs"
INPUT_FILE = "day_06.txt"
input_path = f"{INPUT_PREFIX}/{INPUT_FILE}"

### PART ONE
f_in = open(input_path, 'r')
input = next(f_in)

for idx in range(3, len(input)):
    chars = set()
    for i in range(4):
        chars.add(input[idx-i])
    if len(chars) == 4:
        print(idx+1)
        break

### PART TWO
f_in = open(input_path, 'r')
input = next(f_in)

for idx in range(13, len(input)):
    chars = set()
    for i in range(14):
        chars.add(input[idx-i])
    if len(chars) == 14:
        print(idx+1)
        break


