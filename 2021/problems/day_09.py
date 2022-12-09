INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2021/inputs"
input_path = f"{INPUT_PREFIX}/day_09.txt"

f_in = open(input_path)
grid = []

while True:
    try:
        line = next(f_in).strip()
        lv = [int(v) for v in line]
        grid.append(lv)
    except StopIteration:
        break

dx, dy = [0, 0, 1, -1], [1, -1, 0 ,0]
tot = 0
N, M = len(grid), len(grid[0])
low_points = []


### PART ONE
for i in range(N):
    for j in range(M):
        val = grid[i][j]
        valid = True
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            if nx >= 0 and nx < N and ny >= 0 and ny < M:
                if grid[nx][ny] <= val:
                    valid = False
                    break
        if valid is True:
            low_points.append((i, j))
            tot += 1 + val

print(tot)

### PART TWO
basin_sizes = []
for lp in low_points:
    i, j = lp
    visited = set()
    cur_point = [(i, j)]
    while len(cur_point) > 0:
        cx, cy = cur_point.pop()
        visited.add((cx, cy))
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if nx >= 0 and nx < N and ny >= 0 and ny < M:
                if grid[nx][ny] > grid[cx][cy] and grid[nx][ny] != 9:
                    if (nx, ny) not in visited:
                        cur_point.append((nx, ny))
    basin_sizes.append(len(visited))

basin_sizes = sorted(basin_sizes, reverse=True)
print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])
