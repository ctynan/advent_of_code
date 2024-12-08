INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2024/inputs"
input_path = f"{INPUT_PREFIX}/day_08.txt"

f_in = open(input_path)
grid = []

for line in f_in.readlines():
    line = line.strip()
    grid.append(line)

antenna_locations = dict()
N, M = len(grid), len(grid[0])

for i, v in enumerate(grid):
    for j, w in enumerate(v):
        if grid[i][j] != '.':
            cv = antenna_locations.get(grid[i][j], set())
            cv.add((i,j))
            antenna_locations[grid[i][j]] = cv

### PART ONE
antinodes = set()

for _, v in antenna_locations.items():
    locs = list(v)
    for i, loc_a in enumerate(locs):
        for j, loc_b in enumerate(locs):
            if i == j:
                continue
            else:
                x1, y1 = loc_a
                x2, y2 = loc_b
                if x2 < x1:
                    continue
                else:
                    ax = x1 + (x1-x2)
                    ay = y1 + (y1-y2)
                    if ax >= 0 and ax < N and ay >= 0 and ay < M:
                        antinodes.add((ax,ay))
                    ax = x2 + (x2-x1)
                    ay = y2 + (y2-y1)
                    if ax >= 0 and ax < N and ay >= 0 and ay < M:
                        antinodes.add((ax,ay))

print(len(antinodes))

### PART TWO
def is_inline(x, y, locs):
    for _, loc_a in enumerate(locs):
        for _, loc_b in enumerate(locs):
            if loc_a == loc_b:
                continue
            else:
                x1, y1 = loc_a
                x2, y2 = loc_b
                if x2 < x1:
                    continue
                elif x1 == x2:
                    if x == x1:
                        return True
                    else:
                        continue
                else:
                    m = (y2-y1) / (x2-x1)
                    b = y1 - m*x1
                    if abs(y - (b + m*x)) < 1e-9:
                        return True

    return False

tot = 0
for i in range(N):
    for j in range(M):
        for _, v in antenna_locations.items():
            locs = list(v)
            if is_inline(i, j, locs):
                tot += 1
                break

print(tot)


    