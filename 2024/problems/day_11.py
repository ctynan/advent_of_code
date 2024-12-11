INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2024/inputs"
input_path = f"{INPUT_PREFIX}/day_11.txt"

f_in = open(input_path)
for line in f_in.readlines():
    line = line.strip()

stones = list(map(int, line.split()))

### PART ONE
def run_blink(stones):
    ret = []
    for i, v in enumerate(stones):
        M = len(str(v))
        if v == 0:
            ret.append(1)
        elif M % 2 == 0:
            ret.append(int(str(v)[:(M//2)]))
            ret.append(int(str(v)[(M//2):]))
        else:
            ret.append(2024 * v)
    return ret

### PART TWO
def run_stone_count(stones):
    ret = dict()
    for k, v in stones.items():
        M = len(str(k))
        if k == 0:
            if 1 in ret:
                ret[1] += v
            else:
                ret[1] = v
        elif M % 2 == 0:
            nx, ny = int(str(k)[:(M//2)]), int(str(k)[(M//2):])
            if nx in ret:
                ret[nx] += v
            else:
                ret[nx] = v
            if ny in ret:
                ret[ny] += v
            else:
                ret[ny] = v
        else:
            nx = 2024 * k
            if nx in ret:
                ret[nx] += v
            else:
                ret[nx] = v
    return ret

stones_count = dict()
for v in stones:
    if v in stones_count:
        stones_count[v] += 1
    else:
        stones_count[v] = 1

for idx in range(75):
    stones_count = run_stone_count(stones_count)
    tot = sum([v for _, v in stones_count.items()])
    print(idx, tot)
