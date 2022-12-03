INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/problems/inputs"
INPUT_FILE = "day_03.txt"
input_path = f"{INPUT_PREFIX}/{INPUT_FILE}"
f_in = open(input_path)

def priority(v):
    v_lower = v.lower()
    return 1 + ord(v_lower) - ord('a') + (26 if v.isupper() else 0)


### PART ONE
tot = 0
for line in f_in.readlines():
    num_items = len(line)
    sack_one, sack_two = line[:(num_items // 2)], line[(num_items // 2):]
    common_items = set()
    for v in sack_one:
        if v in sack_two and v not in common_items:
            common_items.add(v)
            tot += priority(v)

print(tot)

### PART TWO
tot = 0
f_in = open(input_path)
while True:
    try:
        sack_one = next(f_in)
        sack_two = next(f_in)
        sack_three = next(f_in)
    except StopIteration:
        break
    for v in sack_one:
        if v in sack_two and v in sack_three:
            tot += priority(v)
            break
print(tot)
