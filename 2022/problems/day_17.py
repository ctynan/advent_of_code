INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2022/inputs"
input_path = f"{INPUT_PREFIX}/day_17.txt"

f_in = open(input_path, 'r')

BLOCKS_X = [ [0, 1, 2, 3], [0, 1, 1, 1, 2], [0, 1, 2, 2, 2], [0, 0, 0 ,0], [0, 0, 1, 1]]
BLOCKS_Y = [ [0, 0, 0 ,0], [1, 1, 0, 2, 1], [0, 0, 0, 1, 2], [0, 1, 2, 3], [0, 1, 0, 1]]
JETS = next(f_in).strip()

### PART ONE

jet_idx = 0
M = len(JETS)
blocks_fallen = 0
FIXED_POINTS = set()
for idx in range(7):
    FIXED_POINTS.add((idx, -1))

while blocks_fallen < 2022:
    import copy
    cur_block_X = copy.deepcopy(BLOCKS_X[blocks_fallen % 5])
    cur_block_Y = copy.deepcopy(BLOCKS_Y[blocks_fallen % 5])
    high_point = max([y for x, y in FIXED_POINTS])
    cur_block_X = list(map(lambda x : x + 2, cur_block_X))
    cur_block_Y = list(map(lambda y : y + 4 + high_point, cur_block_Y))
    
    ### JET PUSH
    while True:
        ### JET
        if JETS[jet_idx % M] == '<' and cur_block_X[0] > 0:
            ### check if shift is possible
            cur_block_X = list(map(lambda x: x - 1, cur_block_X))
            for idx, x in enumerate(cur_block_X):
                if (x, cur_block_Y[idx]) in FIXED_POINTS:
                    cur_block_X = list(map(lambda x: x + 1, cur_block_X))
                    break
        elif JETS[jet_idx % M] == '>' and cur_block_X[-1] < 6:
            cur_block_X = list(map(lambda x: x + 1, cur_block_X))
            for idx, x in enumerate(cur_block_X):
                if (x, cur_block_Y[idx]) in FIXED_POINTS:
                    cur_block_X = list(map(lambda x: x -1, cur_block_X))
                    break
        jet_idx += 1
        ### FALL
        cur_block_Y = list(map(lambda y: y - 1, cur_block_Y))
        ### COLLISION CHECK
        collision_flag = False
        for idx, v in enumerate(cur_block_Y):
            if (cur_block_X[idx], v) in FIXED_POINTS:
                collision_flag = True
                cur_block_Y = list(map(lambda y: y + 1, cur_block_Y))
                break
        if collision_flag:
            for idx, y in enumerate(cur_block_Y):
                # HIGH_BLOCK[cur_block_X[idx]] = max(HIGH_BLOCK[cur_block_X[idx]], y)
                FIXED_POINTS.add((cur_block_X[idx], y))
            blocks_fallen += 1
            break

print(1+max([y for x, y in FIXED_POINTS]))

### PART TWO

jet_idx = 0
M = len(JETS)
blocks_fallen = 0
FIXED_POINTS = set()
HIGH_BLOCKS = []
for idx in range(7):
    FIXED_POINTS.add((idx, -1))

def end_point_exists(point, point_set):
    x, y = point
    if x == 6:
        return True, [y]
    else:
        if (x + 1, y - 1) in point_set:
            ret, v = end_point_exists((x + 1, y - 1), point_set)
            if ret is True:
                return True, [y-1] + v 
        if (x + 1, y) in point_set:
            ret, v = end_point_exists((x + 1, y), point_set)
            if ret is True:
                return True, [y] + v
        if (x + 1, y + 1) in point_set:
            ret, v = end_point_exists((x + 1, y + 1), point_set)
            if ret is True:
                return True, [y+1] + v
    return False, []

def update_points(points):
    new_points = copy.deepcopy(points)
    point_list = list(points)
    from operator import itemgetter
    point_list = sorted(point_list, key=itemgetter(1), reverse=True)
    for p in points:
        x, y = p
        if x != 0:
            continue
        else:
            line, line_points = end_point_exists((x, y), points)
            if line is True:
                new_points = set()
                for v in points:
                    x, y = v
                    if y < line_points[x]:
                        continue
                    else:
                        new_points.add((x,y))
                pass
    return new_points

NUM = 1000000000000
div = NUM % 5*M
mult = (NUM - div) // 5*M
import time
ts = time.monotonic()

TOP_ROWS_HASH = [] ### for cycle checking
from collections import Counter
def generate_top_rows_hash(num_rows, jet_mod, block_mod):
    global FIXED_POINTS
    top_point = max([y for x, y in FIXED_POINTS])
    hash_value = 0
    for j in range(num_rows):
        for x in range(7):
            exponent = 2**(7*j + x)
            if (x, top_point-j) in FIXED_POINTS:
                hash_value += exponent
    hash_value += 2**(7*num_rows)*(5*jet_mod + block_mod)
    
    return hash_value

while blocks_fallen < 100000:
    if (blocks_fallen+1) % 1000 == 0:
        print("Blocks fallen: ", blocks_fallen+1, time.monotonic()-ts) 
    cur_block_X = copy.deepcopy(BLOCKS_X[blocks_fallen % 5])
    cur_block_Y = copy.deepcopy(BLOCKS_Y[blocks_fallen % 5])
    high_point = max([y for x, y in FIXED_POINTS])
    cur_block_X = list(map(lambda x : x + 2, cur_block_X))
    cur_block_Y = list(map(lambda y : y + 4 + high_point, cur_block_Y))
    
    ### JET PUSH
    while True:
        ### JET
        if JETS[jet_idx % M] == '<' and cur_block_X[0] > 0:
            ### check if shift is possible
            cur_block_X = list(map(lambda x: x - 1, cur_block_X))
            for idx, x in enumerate(cur_block_X):
                if (x, cur_block_Y[idx]) in FIXED_POINTS:
                    cur_block_X = list(map(lambda x: x + 1, cur_block_X))
                    break
        elif JETS[jet_idx % M] == '>' and cur_block_X[-1] < 6:
            cur_block_X = list(map(lambda x: x + 1, cur_block_X))
            for idx, x in enumerate(cur_block_X):
                if (x, cur_block_Y[idx]) in FIXED_POINTS:
                    cur_block_X = list(map(lambda x: x -1, cur_block_X))
                    break
        jet_idx += 1
        ### FALL
        cur_block_Y = list(map(lambda y: y - 1, cur_block_Y))
        ### COLLISION CHECK
        collision_flag = False
        for idx, v in enumerate(cur_block_Y):
            if (cur_block_X[idx], v) in FIXED_POINTS:
                collision_flag = True
                cur_block_Y = list(map(lambda y: y + 1, cur_block_Y))
                break
        if collision_flag:
            for idx, y in enumerate(cur_block_Y):
                FIXED_POINTS.add((cur_block_X[idx], y))
            blocks_fallen += 1
            # if blocks_fallen % 1000 == 0:
            #     FIXED_POINTS = update_points(FIXED_POINTS)
            HIGH_BLOCKS.append(max([y for x, y in FIXED_POINTS]))
            break
    
    TOP_ROWS_HASH.append(generate_top_rows_hash(6, (jet_idx-1)%M, (blocks_fallen-1)%5))
    from collections import Counter
    c = Counter(TOP_ROWS_HASH)
    tmp = c.most_common(1)[0]
    if tmp[1] >= 5:
        for hash_idx, hash_val in enumerate(TOP_ROWS_HASH):
            if hash_val == tmp[0]:
                ### THIS GIVES YOU THE CYCLE INFO MANUALLY INPUTTED BELOW
                print(hash_idx, HIGH_BLOCKS[hash_idx])
        break


y = NUM - 178
CYCLE_LENGTH = 1908 - 178
y_mod = y % CYCLE_LENGTH
tot = 282
tot += (2941-282) * ((y - y_mod) // CYCLE_LENGTH)
tot += HIGH_BLOCKS[178 + y_mod] - HIGH_BLOCKS[178]
print(tot)
### let y =
### 31 + (1000000000000 - 17 )