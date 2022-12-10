INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2021/inputs"
input_path = f"{INPUT_PREFIX}/day_11.txt"

def iterate_grid(grid):
    N, M = len(grid), len(grid[0])
    dx = [1, 1, 1, 0, 0, -1, -1, -1]
    dy = [1, 0, -1, 1, -1, 1, 0, -1]
    flashes_this_iteration = set()
    flashes = []
    for i in range(N):
        for j in range(M):
            grid[i][j] += 1
            if grid[i][j] > 9:
                flashes.append((i,j))
    while len(flashes) > 0:
        cx, cy = flashes.pop(0)
        if (cx, cy) in flashes_this_iteration:
            continue
        flashes_this_iteration.add((cx,cy))
        for z in range(8):
            nx = cx + dx[z]
            ny = cy + dy[z]
            if nx >= 0 and nx < N and ny >= 0 and ny < M:
                grid[nx][ny] += 1
                if grid[nx][ny] > 9:
                    if (nx, ny) not in flashes_this_iteration:
                        flashes.append((nx, ny))
    
    for v in flashes_this_iteration:
        cx, cy = v
        grid[cx][cy] = 0
                
    return grid, len(flashes_this_iteration) 

### PART ONE
f_in = open(input_path)
grid = []
while True:
    try:
        line = next(f_in).strip()
    except StopIteration:
        break
    grid.append([int(v) for v in line])

num_flashes = 0
for _ in range(100):
    grid, cycle_flashes = iterate_grid(grid)
    num_flashes += cycle_flashes
    
print(num_flashes)

### PART TWO
f_in = open(input_path)
grid = []

while True:
    try:
        line = next(f_in).strip()
    except StopIteration:
        break
    grid.append([int(v) for v in line])

num_flashes = 0
for idx in range(10000):
    grid, cycle_flashes = iterate_grid(grid)
    if cycle_flashes == 100:
        print(idx+1)
        break


