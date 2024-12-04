import os
INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2024/inputs"
input_path = f"{INPUT_PREFIX}/day_04.txt"


f_in = open(input_path)
grid = []

for line in f_in.readlines():
    line = line.strip()
    grid.append(line)

N, M = len(grid), len(grid[0])

### PART ONE
dx = [1, 1, 1, -1, -1, -1, 0, 0]
dy = [1, 0, -1, 1, 0, -1, 1, -1]
xmas_chars = ['X', 'M', 'A', 'S']
cnt = 0

for i in range(N):
    for j in range(M):
        for z in range(len(dx)):
            valid_xmas = True
            for idx, v in enumerate(xmas_chars):
                nx = i + idx*dx[z]
                ny = j + idx*dy[z]
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    valid_xmas = False
                    break
                else:
                    if grid[nx][ny] != v:
                        valid_xmas = False
                        break
            
            cnt += 1 if valid_xmas else 0

print(cnt)

### PART TWO
cnt = 0

for i in range(N):
    for j in range(M):
        if grid[i][j] != 'A':
                continue
        else:
            lx, ly, rx, ry = i-1, j-1, i+1, j+1
            if lx < 0 or lx >= N or rx < 0 or rx >= N or ly < 0 or ly >= M or ry < 0 or ry >= M:
                continue
            
            if (grid[lx][ly] == 'M' and grid[rx][ry] == 'S') or (grid[lx][ly] == 'S' and grid[rx][ry] == 'M'):
                pass
            else:
                continue
            
            lx, ly, rx, ry = i-1, j+1, i+1, j-1
            if lx < 0 or lx >= N or rx < 0 or rx >= N or ly < 0 or ly >= M or ry < 0 or ry >= M:
                continue
            
            if (grid[lx][ly] == 'M' and grid[rx][ry] == 'S') or (grid[lx][ly] == 'S' and grid[rx][ry] == 'M'):
                pass
            else:
                continue
            
            cnt += 1

print(cnt)