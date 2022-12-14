INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2022/inputs"
input_path = f"{INPUT_PREFIX}/day_14.txt"

f_in = open(input_path)
path_points = set()

while True:
    try:
        line = next(f_in).strip().split('->')
        vals = list(map(lambda x : x.split(','), line))
        vals = [(int(v[0]), int(v[1])) for v in vals] 
        for idx, v in enumerate(line):
            if idx == 0:
                continue
            cx, cy = vals[idx-1]
            nx, ny = vals[idx]
            diff = abs(cx-nx) + abs(cy-ny) + 1
            for i in range(diff):
                pos_x = cx + i * (1 if nx > cx else -1) * (0 if nx == cx else 1) 
                pos_y = cy + i * (1 if ny > cy else -1) * (0 if ny == cy else 1)
                path_points.add((pos_x, pos_y))
    except StopIteration:
        break

def lay_sand(cx, cy, points, hi_y, floor=False):
    if floor is True and cy + 1 == hi_y:
        points.add((cx,cy))
        return 0
    elif floor is False and cy > hi_y:
        return -1
    elif (cx, cy+1) not in path_points:
        return lay_sand(cx, cy+1, points, hi_y, floor)
    elif (cx-1, cy+1) not in path_points:
        return lay_sand(cx-1, cy+1, points, hi_y, floor)
    elif (cx+1, cy+1) not in path_points:
        return lay_sand(cx+1, cy+1, points, hi_y, floor)
    else:
        points.add((cx, cy))
        return 1

### PART ONE
hi_y = max([y for _, y in path_points])
tot = 0
while True:
    ret_status = lay_sand(cx=500, cy=0, points=path_points, hi_y=hi_y, floor=False)
    if ret_status == -1:
        break
    else:
        tot += 1

print(tot)

### PART TWO
f_in = open(input_path)
path_points = set()
while True:
    try:
        line = next(f_in).strip().split('->')
        vals = list(map(lambda x : x.split(','), line))
        vals = [(int(v[0]), int(v[1])) for v in vals] 
        for idx, v in enumerate(line):
            if idx == 0:
                continue
            cx, cy = vals[idx-1]
            nx, ny = vals[idx]
            diff = abs(cx-nx) + abs(cy-ny) + 1
            for i in range(diff):
                pos_x = cx + i * (1 if nx > cx else -1) * (0 if nx == cx else 1) 
                pos_y = cy + i * (1 if ny > cy else -1) * (0 if ny == cy else 1)
                path_points.add((pos_x, pos_y))
    except StopIteration:
        break

hi_y = max([y for _, y in path_points]) + 2
tot = 0
while True:
    ret_status = lay_sand(cx=500, cy=0, points=path_points, hi_y=hi_y, floor=True)
    tot += 1
    if (500, 0) in path_points:
        break

print(tot)