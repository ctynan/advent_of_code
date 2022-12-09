INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2021/inputs"
input_path = f"{INPUT_PREFIX}/day_07.txt"

f_in = open(input_path)

positions = list(map(int, next(f_in).strip().split(',')))

### PART ONE
lo, hi = min(positions), max(positions)
best = 10**9
for x in range(lo, hi+1):
    tot = 0
    for v in positions:
        tot += abs(v-x)
    best = min(best ,tot)

print(best)

### PART TWO
triangle_numbers = [(v * (v+1))//2 for v in range(5000)]
best = 10**9
for x in range(lo, hi+1):
    tot = 0
    for v in positions:
        tot += triangle_numbers[abs(v-x)]
    best = min(best ,tot)

print(best)