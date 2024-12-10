INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2024/inputs"
input_path = f"{INPUT_PREFIX}/day_10.txt"

f_in = open(input_path)
grid = []
for line in f_in.readlines():
    line = line.strip()
    row = [int(v) for v in line]
    grid.append(row)

N, M = len(grid), len(grid[0])

### PART ONE
tot = 0
def score(x, y, grid):
    if grid[x][y] > 0:
        return 0
    visited_points, q = set(), set()
    summits = set()
    q.add((x,y))
    visited_points.add((x,y))
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    
    while len(q) > 0:
        cx, cy = q.pop()
        if grid[cx][cy] == 9:
            summits.add((cx,cy))
        for z in range(len(dx)):
            nx, ny = cx + dx[z], cy + dy[z]
            if nx >= 0 and nx < N and ny >= 0 and ny < M:
                if (nx, ny) not in visited_points and grid[nx][ny] == grid[cx][cy] + 1:
                    q.add((nx, ny))
                    visited_points.add((nx, ny))
    
    return len(summits)

for i in range(N):
    for j in range(M):
        tot += score(i, j, grid)

print(tot)

### PART TWO
def number_trails(x, y, grid):
    if grid[x][y] > 0:
        return 0
    q = list()
    summits = 0
    q.append((x,y))
    # visited_points.add((x,y))
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    
    while len(q) > 0:
        cx, cy = q.pop()
        if grid[cx][cy] == 9:
            summits += 1
        for z in range(len(dx)):
            nx, ny = cx + dx[z], cy + dy[z]
            if nx >= 0 and nx < N and ny >= 0 and ny < M:
                if grid[nx][ny] == grid[cx][cy] + 1:
                    q.append((nx, ny))
    
    return summits

tot = 0
for i in range(N):
    for j in range(M):
        tot += number_trails(i, j, grid)

print(tot)