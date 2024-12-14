INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2024/inputs"
input_path = f"{INPUT_PREFIX}/day_14.txt"

f_in = open(input_path)
pos, vel = [], []
for line in f_in.readlines():
    line = line.strip()
    line = line.replace('p=', '').replace('v=', '').replace(',', ' ')
    lv = list(map(int, line.split()))
    pos.append((lv[0], lv[1]))
    vel.append((lv[2], lv[3]))

N, M = 101, 103
secs = 100
new_pos = []

for idx, v in enumerate(pos):
    x, y = v
    vx, vy = vel[idx]
    nx = (x + vx * secs) % N
    ny = (y + vy * secs) % M
    new_pos.append((nx,ny))

quadrant_count = [0, 0, 0, 0]
print(new_pos)

for v in new_pos:
    x, y = v
    if x == (N-1) // 2 or y == (M-1) // 2:
        continue
    quadrant_idx = 1 if x < N // 2 else 0 
    quadrant_idx += 2 if y < M // 2 else 0
    quadrant_count[quadrant_idx] += 1

print(quadrant_count[0] * quadrant_count[1] * quadrant_count[2]*quadrant_count[3])

def visualise_pos(pos, vel, secs, N, M):
    new_pos = set()
    for idx, v in enumerate(pos):
        x, y = v
        vx, vy = vel[idx]
        nx = (x + vx * secs) % N
        ny = (y + vy * secs) % M
        new_pos.add((nx,ny))
    print(f"Image at time: {secs}")
    for i in range(N):
        x = ""
        for j in range(M):
            x += '*' if (i,j) in new_pos else ' '
        print(x)

# Two components found by inspection
# Component one 74 + 101*i
visualise_pos(pos, vel, 74, N, M)
visualise_pos(pos, vel, 175, N, M)
visualise_pos(pos, vel, 276, N, M)
# Component two 19 + 103*i
visualise_pos(pos, vel, 19, N, M)
visualise_pos(pos, vel, 122, N, M)
visualise_pos(pos, vel, 225, N, M)

# Find lcm and print
for i in range(100000):
    if (i-74) % 101 == 0 and (i-19) % 103 == 0:
        visualise_pos(pos, vel, i, N, M)
        break