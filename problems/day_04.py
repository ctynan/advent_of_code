INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/problems/inputs"
INPUT_FILE = "day_04.txt"
input_path = f"{INPUT_PREFIX}/{INPUT_FILE}"
f_in = open(input_path)

### PART ONE
tot = 0
for line in f_in.readlines():
    elf_one, elf_two = line.split(',')
    elf_one = list(map(int, elf_one.split('-')))
    elf_two = list(map(int, elf_two.split('-')))
    e1_lo, e1_hi = elf_one[0], elf_one[1]
    e2_lo, e2_hi = elf_two[0], elf_two[1]

    if (e1_lo <= e2_lo and e1_hi >= e2_hi) or (e1_lo >= e2_lo and e1_hi <= e2_hi):
        tot += 1

print(tot)

### PART TWO
tot = 0
f_in = open(input_path)
for line in f_in.readlines():
    elf_one, elf_two = line.split(',')
    elf_one = list(map(int, elf_one.split('-')))
    elf_two = list(map(int, elf_two.split('-')))
    e1_lo, e1_hi = elf_one[0], elf_one[1]
    e2_lo, e2_hi = elf_two[0], elf_two[1]

    if e1_hi < e2_lo or e1_lo > e2_hi:
        tot += 0
    else:
        tot += 1
print(tot)