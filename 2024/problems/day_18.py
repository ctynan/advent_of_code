INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2024/inputs"
input_path = f"{INPUT_PREFIX}/day_18.txt"

f_in = open(input_path)
particles = []
for line in f_in.readlines():
    line = line.strip()
    lv = list(map(int, line.split(',')))
    particles.append((lv[0], lv[1]))

N, M = 71, 71
grid = [[0 for _ in range(M)] for _ in range(N)]

def find_shortest_path(grid):
    N, M = len(grid), len(grid[0])
    dp = [[None for _ in range(M)] for _ in range(N)]
    dp[0][0] = 0
    q = set()
    q.add((0,0))

    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    while len(q) > 0:
        cx, cy = q.pop()
        for idx in range(4):
            nx, ny = cx + dx[idx], cy + dy[idx]
            if nx >= 0 and nx < N and ny >= 0 and ny < M:
                if grid[nx][ny] == 0:
                    if dp[nx][ny] is None:
                        dp[nx][ny] = 1 + dp[cx][cy]
                        q.add((nx,ny))
                    else:
                        pass
                else:
                    pass
            else:
                pass

    return dp[-1][-1]

### PART ONE
for idx in range(1024):
    x, y = particles[idx]
    grid[x][y] = 1

print(find_shortest_path(grid))

### PART TWO
grid = [[0 for _ in range(M)] for _ in range(N)]

for idx, v in enumerate(particles):
    x, y = v
    grid[x][y] = 1
    if find_shortest_path(grid) is None:
        print(f"{x},{y}")
        break
