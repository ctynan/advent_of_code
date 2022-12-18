INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2022/inputs"
input_path = f"{INPUT_PREFIX}/day_18.txt"

f_in = open(input_path, 'r')

cubes = []
while True:
    try:
        line = tuple(map(int, next(f_in).strip().split(',')))
        cubes.append(line)
    except StopIteration:
        break

### PART ONE
N = len(cubes)
tot = 6*N
for i, v1 in enumerate(cubes):
    for j,v2 in enumerate(cubes):
        if j <= i:
            continue
        a, b, c = v1
        x, y, z = v2
        if abs(x-a) + abs(y-b) + abs(z-c) == 1:
            tot -= 2

print(tot)
        
### PART TWO
for idx in range(3):
    print(min([v[idx] for v in cubes]), max([v[idx] for v in cubes]))
cubes = list(map(lambda x: (x[0]+1, x[1]+1, x[2]+1), cubes))
M = 22
grid = []
for _ in range(M):
    ng = []
    for _ in range(M):
        ng.append([0 for _ in range(M)])
    grid.append(ng)

lava_set = set()
for v in cubes:
    lava_set.add(v)
points = [(0,0,0)]
dx = [1, -1, 0, 0, 0 ,0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

reachable_sides = []
for _ in range(N):
    reachable_sides.append([0 for _ in range(6)])

while len(points) > 0:
    x, y, z = points.pop(0)
    grid[x][y][z] = 1
    for k in range(6):
        nx, ny, nz = x + dx[k], y + dy[k], z + dz[k]
        if nx >= 0 and nx < M and ny >= 0 and ny < M and nz >=0 and nz < M:
            if grid[nx][ny][nz] == 0:
                if (nx, ny, nz) not in lava_set:
                    if (nx, ny, nz) not in points:
                        points.append((nx, ny, nz))
                else:
                    cube_idx = cubes.index((nx, ny, nz))
                    reachable_sides[cube_idx][k] = 1

tot = sum([sum(v) for v in reachable_sides])
print(tot)
