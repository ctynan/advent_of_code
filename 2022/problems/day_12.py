INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2022/inputs"
input_path = f"{INPUT_PREFIX}/day_12.txt"

f_in = open(input_path, 'r')

grid = []
while True:
    try:
        line = next(f_in)
        grid.append(line.strip())
    except StopIteration:
        break

def solve(grid, use_a=False):
    N, M = len(grid), len(grid[0])
    best = []
    elevs = []
    for _ in range(N):
        best.append([2*N*M for _ in range(M)])
        elevs.append([0 for _ in range(M)])

    pos = []
    for r_idx, row in enumerate(grid):
        for c_idx, v in enumerate(row):
            if v == 'S':
                pos.append((r_idx, c_idx))
                best[r_idx][c_idx] = 0
                elevs[r_idx][c_idx] = 1
            elif v == 'E':
                elevs[r_idx][c_idx] = 26
            elif v == 'a' and use_a is True:
                pos.append((r_idx, c_idx))
                best[r_idx][c_idx] = 0
                elevs[r_idx][c_idx] = 1
            else:
                elevs[r_idx][c_idx] = ord(v) - ord('a') + 1

    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    while len(pos) > 0:
        cx, cy = pos.pop(0)
        if grid[cx][cy] == 'E':
            print(best[cx][cy])
        for z in range(4):
            nx, ny = cx + dx[z], cy + dy[z]
            if nx >= 0 and nx < N and ny >= 0 and ny < M:
                if elevs[nx][ny] - elevs[cx][cy] <= 1:
                    if best[nx][ny] == 2*N*M:
                        best[nx][ny] = best[cx][cy] + 1
                        pos.append((nx,ny))
        
    return

solve(grid)
solve(grid, use_a=True)