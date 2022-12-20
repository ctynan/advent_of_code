INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2022/inputs"
input_path = f"{INPUT_PREFIX}/day_20.txt"

f_in = open(input_path, 'r')

vals = []
while True:
    try:
        v = int(next(f_in).strip())
        vals.append(v)
    except StopIteration:
        break

def shift(x, orig_idx, i):
    N = len(x)
    idx = orig_idx.index(i)
    val = x[idx]
    new_pos = (idx + val) % (N-1)
    _, _ = x.pop(idx), orig_idx.pop(idx)
    return x[:(new_pos)]+[val]+x[(new_pos):], orig_idx[:(new_pos)]+[i]+orig_idx[(new_pos):]

N = len(vals)
orig_idx = list(range(N))

import copy
v_hard = copy.deepcopy(vals)

### PART ONE
for i in range(N):
    vals, orig_idx = shift(vals, orig_idx, i)
    
zero_idx = vals.index(0)
print(sum([vals[(zero_idx + 1000*i) %N] for i in range(1,4)]))

### PART TWO
vals = list(map(lambda x : 811589153 * x, v_hard))
orig_idx = list(range(N))

for t in range(10):
    for i in range(N):
        vals, orig_idx = shift(vals, orig_idx, i)
    # print(t, vals)

zero_idx = vals.index(0)
print(sum([vals[(zero_idx + 1000*i) %N] for i in range(1,4)]))