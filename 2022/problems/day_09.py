INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2022/inputs"
input_path = f"{INPUT_PREFIX}/day_09.txt"

DIRS = {'R' : (1, 0), 'L' : (-1, 0), 'U' : (0, 1), 'D' : (0, -1)}

def calc_next_move(H_cx, H_cy, T_cx, T_cy):
    l1_dist = abs(H_cx - T_cx) + abs(H_cy - T_cy)

    if l1_dist <= 1:
        pass
    elif l1_dist == 2:
        if H_cx - T_cx == 2 and H_cy == T_cy:
            T_cx += 1
        elif H_cx - T_cx == -2 and H_cy == T_cy:
            T_cx -= 1
        elif H_cx - T_cx == 0 and H_cy - T_cy == 2:
            T_cy += 1
        elif H_cx - T_cx == 0 and H_cy - T_cy == -2:
            T_cy -= 1
    else:
        nx = 1 if H_cx > T_cx else -1
        ny = 1 if H_cy > T_cy else -1
        T_cx += nx
        T_cy += ny

    return T_cx, T_cy

### PART ONE
f_in = open(input_path)
positions = set()
positions.add((0,0))
H_cx, H_cy, T_cx, T_cy = 0, 0, 0, 0

while True:
    try:
        line = next(f_in).strip().split()
        direction, num_steps = line[0], int(line[1])
    except StopIteration:
        break

    dx, dy = DIRS[direction]
    for _ in range(num_steps):
        H_cx += dx
        H_cy += dy

        T_cx, T_cy = calc_next_move(H_cx, H_cy, T_cx, T_cy)
        positions.add((T_cx, T_cy))

print(len(positions))

### PART TWO
f_in = open(input_path)
positions = set()
positions.add((0,0))
cur_pos = [(0,0) for _ in range(10)]

while True:
    try:
        line = next(f_in).strip().split()
        direction, num_steps = line[0], int(line[1])
    except StopIteration:
        break

    dx, dy = DIRS[direction]
    for _ in range(num_steps):
        cur_pos[0] = (cur_pos[0][0] + dx, cur_pos[0][1] + dy)
        for idx in range(10):
            if idx == 0:
                continue
            else:
                H_cx, H_cy = cur_pos[idx-1]
                T_cx, T_cy = cur_pos[idx]
                T_cx, T_cy = calc_next_move(H_cx, H_cy, T_cx, T_cy)
                cur_pos[idx] = (T_cx, T_cy)
        
        positions.add(cur_pos[-1])

print(len(positions))






