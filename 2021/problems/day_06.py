INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2021/inputs"
input_path = f"{INPUT_PREFIX}/day_06.txt"

f_in = open(input_path)
num_fish = [0 for _ in range(10)]

inp = list(map(int, next(f_in).strip().split(',')))
for v in inp:
    num_fish[v] += 1

for t in range(256):
    new_fish_counts = [0 for _ in range(10)]
    for idx, v in enumerate(num_fish):
        if idx == 0:
            new_fish_counts[6] += v
            new_fish_counts[8] += v
        else:
            new_fish_counts[idx-1] += v
    num_fish = new_fish_counts
    print(t, sum(new_fish_counts))