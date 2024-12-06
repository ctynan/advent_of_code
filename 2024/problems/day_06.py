import os
INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2024/inputs"
input_path = f"{INPUT_PREFIX}/day_06.txt"

f_in = open(input_path)
grid = []

for line in f_in.readlines():
    line = line.strip()
    row = []
    for v in line:
        if v == '.':
            row.append(0)
        elif v == '#':
            row.append(1)
        elif v == '^':
            row.append(2)
        else:
            pass
    grid.append(row)

N, M = len(grid), len(grid[0])
start_x, start_y, dir = None, None, 0

for x in range(N):
    for y in range(M):
        if grid[x][y] == 2:
            start_x, start_y = x, y
            grid[x][y] = 0
            break

### PART ONE
cx, cy = start_x, start_y
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
visited = set()
visited.add((cx, cy))
while True:
    visited.add((cx, cy))
    nx, ny = cx + dx[dir], cy + dy[dir]
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        break
    if grid[nx][ny] == 0:
        cx, cy = nx, ny
    else:
        dir = (dir + 1) % 4

print(len(visited))

### PART TWO
def is_loop(grid, start_x, start_y):
    visited_states = set()
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    cx, cy, dir = start_x, start_y, 0
    while True:
        if (cx, cy, dir) in visited_states:
            return True
        else:
            visited_states.add((cx, cy, dir))
        nx, ny = cx + dx[dir], cy + dy[dir]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            break
        if grid[nx][ny] == 0:
            cx, cy = nx, ny
        else:
            dir = (dir + 1) % 4
    
    return False

tot = 0
for i in range(N):
    for j in range(M):
        if grid[i][j] == 0 and (i,j) != (start_x, start_y):
            grid[i][j] = 1
            tot += is_loop(grid, start_x, start_y)
            grid[i][j] = 0

print(tot)
