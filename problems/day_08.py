INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/problems/inputs"
input_path = f"{INPUT_PREFIX}/day_08.txt"

f_in = open(input_path)
trees = []
while True:
    try:
        line = list(map(int, next(f_in).strip()))
        trees.append(line)
    except StopIteration:
        break


N, M = len(trees), len(trees[0])
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
tot = 0

### PART ONE
for i in range(N):
    for j in range(M):
        for z in range(4):
            valid = True
            idx = 1
            while True:
                nx = i + idx * dx[z]
                ny = j + idx * dy[z]
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    break
                elif trees[nx][ny] >= trees[i][j]:
                    valid = False
                    break
                else:
                    idx += 1
            if valid is True:
                tot += 1
                break

print(tot)
 
### PART TWO
best = 0
for i in range(N):
    for j in range(M):
        v = 1
        for z in range(4):
            idx = 1
            while True:
                nx = i + idx * dx[z]
                ny = j + idx * dy[z]
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    break
                elif trees[nx][ny] >= trees[i][j]:
                    idx += 1
                    break
                else:
                    idx += 1
            v *= (idx-1)
        best = max(best, v)
            
print(best)
 
        