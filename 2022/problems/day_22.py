INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2022/inputs"
input_path = f"{INPUT_PREFIX}/day_22.txt"

f_in = open(input_path, 'r')

grid = []
while True:
    line = next(f_in)
    if len(line.strip()) > 0:
        row = []
        for char in line:
            if char == ' ':
                row.append('W')
            elif char in ('#', '.'):
                row.append(char)
        grid.append(row)
    else:
        instructions = next(f_in)
        import re
        instructions = re.split('(R|L)', instructions)
        break

### PART ONE
N, M = len(grid), len(grid[0])
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
dir_idx = 0
cx, cy = 0, 0
for idx, v in enumerate(grid[0]):
    if v == '.':
        cy = idx
        break

steps_to_move = int(instructions[0])
instructions_idx = 0

grid_width = max([len(v) for v in grid])
for idx, row in enumerate(grid):
    while len(grid[idx]) < grid_width:
        grid[idx].append('W')

while True:
    ### Need to do a move
    nx, ny = (cx + dx[dir_idx] + N) % N, (cy + dy[dir_idx] + M) % M
    if grid[nx][ny] == '.':
        cx, cy = nx, ny
    elif grid[nx][ny] == '#':
        pass
    elif grid[nx][ny] == 'W':
        while grid[nx][ny] == 'W':
            nx, ny = (nx + dx[dir_idx]) % N, (ny + dy[dir_idx]) % M
            if grid[nx][ny] == '.':
                cx, cy = nx, ny
                break
            elif grid[nx][ny] == '#':
                break
            else:
                pass
    else:
        raise Exception
    
    steps_to_move -= 1
    if steps_to_move == 0:
        print(cx, cy)
        instructions_idx += 1
        if instructions_idx >= len(instructions):
            break
        else:
            change_dir = instructions[instructions_idx]
            if change_dir == 'R':
                dir_idx = (dir_idx+1) % 4
            elif change_dir == 'L':
                dir_idx = (dir_idx+3) % 4
            else:
                raise Exception
            instructions_idx += 1
            steps_to_move = int(instructions[instructions_idx])

print(cx+1, cy+1, dir_idx)
print(1000*(cx+1) + 4*(cy+1) + dir_idx)

### PART TWO

cube = []
sz = 4
for _ in range(sz):
    tmp = []
    for _ in range(sz):
        tmp.append([0 for _ in range(sz)])
    cube.append(tmp)

for i in range(4):
    for j in range(4):
        # front face
        cube[i][j][0] = grid[]

        # top face
        cube[i][3][j] = grid[8+i][3-j]
        # bottom face
        cube[i][0][j] = grid[8+i][]

    