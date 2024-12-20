INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2024/inputs"
input_path = f"{INPUT_PREFIX}/day_20.txt"

f_in = open(input_path)
grid = []

for line in f_in.readlines():
    line = line.strip()
    row = []
    for v in line:
        if v == '#':
            row.append(0)
        elif v == '.':
            row.append(1)
        elif v == 'S':
            row.append(2)
        elif v == 'E':
            row.append(3)
    grid.append(row)

N, M = len(grid), len(grid[0])

for i, row in enumerate(grid):
    for j, v in enumerate(row):
        if v == 2:
            start_x, start_y = i, j
            grid[i][j] = 1
        elif v == 3:
            end_x, end_y = i, j
            grid[i][j] = 1
        else:
            pass

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
cheats = set()
for i in range(N):
    for j in range(M):
        for z1 in range(4):
            for z2 in range(4):
                mx, my = i + dx[z1], j + dy[z1]
                nx, ny = i + dx[z1] + dx[z2], j + dy[z1] + dy[z2]
                if min(nx, mx) >= 0 and max(nx, mx) < N and min(ny, my) >= 0 and max(ny, my) < M:
                    if (nx, ny) != (i, j) and grid[mx][my] == 0 and grid[nx][ny] == 1 and grid[i][j] == 1:
                        cheats.add((i, j, nx, ny))

def run_simulation(grid, start_x, start_y):
    q = set()
    q.add((start_x, start_y))
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    N, M = len(grid), len(grid[0])
    dp = [[None for _ in range(M)] for _ in range(N)]
    dp[start_x][start_y] = 0

    while len(q) > 0:
        cx, cy = q.pop()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < M:
                if grid[nx][ny] == 1:
                    if dp[nx][ny] is None:
                        q.add((nx, ny))
                        dp[nx][ny] = 1 + dp[cx][cy]

        # if (cx, cy) == (cheat_cx, cheat_cy):
        #     if dp[cheat_nx][cheat_ny] is None:
        #         q.add((cheat_nx, cheat_ny))
        #         dp[cheat_nx][cheat_ny] = 2 + dp[cx][cy]

    return dp

### PART ONE 
cost = run_simulation(grid, start_x, start_y)
baseline = cost[end_x][end_y]
tot = 0
for idx, c in enumerate(cheats):
    # cost to the start point of cheat
    cx, cy, nx, ny = c
    start_cost = cost[cx][cy]
    # cost from the end point of the cheat
    end_cost = cost[end_x][end_y] - cost[nx][ny]
    cheat_cost = start_cost + end_cost + 2
    improvement = baseline - cheat_cost
    if improvement >= 100:
        tot += 1

print(tot)

### PART TWO
cheats = set()
for i in range(N):
    for j in range(M):
        for nx in range(N):
            for ny in range(M):
                if (nx, ny) != (i, j) and grid[nx][ny] == 1 and grid[i][j] == 1 and (abs(i-nx) + abs(j-ny)) <= 20:
                    cheats.add((i, j, nx, ny))

tot = 0
times = []
for idx, c in enumerate(cheats):
    # cost to the start point of cheat
    cx, cy, nx, ny = c
    start_cost = cost[cx][cy]
    # cost from the end point of the cheat
    end_cost = cost[end_x][end_y] - cost[nx][ny]
    cheat_cost = start_cost + end_cost + abs(nx-cx) + abs(ny-cy)
    improvement = baseline - cheat_cost
    if improvement >= 100:
        tot += 1
        
print(tot)

