INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2024/inputs"
input_path = f"{INPUT_PREFIX}/day_15.txt"

f_in = open(input_path)
grid, instructions = [], ""
for line in f_in.readlines():
    line = line.strip()
    if '#' in line:
        row = []
        for v in line:
            if v == '#':
                row.append(0) 
            elif v == 'O':
                row.append(1)
            elif v == '.':
                row.append(2)
            elif v == '@':
                row.append(3)
        grid.append(row)
    elif len(line.strip()) > 0:
        instructions += line
    else:
        pass

import copy
start_grid = copy.deepcopy(grid)

cx, cy = None, None
for i, row in enumerate(grid):
    for j, _ in enumerate(row):
        if grid[i][j] == 3:
            cx, cy = i, j
            grid[i][j] = 2

def move_objects(grid, initial_object, instruction):
    cx, cy, rx, ry = initial_object
    dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
    instruction_idx = [idx for idx, v in enumerate(['v', '^', '<', '>']) if v == instruction][0]
    x_delta, y_delta = dx[instruction_idx], dy[instruction_idx]
    
    pushed_objects = set()
    q = set()
    q.add((cx,cy,rx,ry))

    while len(q) > 0:
        cx, cy, rx, ry = q.pop()
        
        pushed_objects.add((cx,cy,rx,ry))
        
        new_cx, new_cy = cx + x_delta, cy + y_delta
        new_rx, new_ry = rx + x_delta, ry + y_delta
        
        if grid[new_cx][new_cy] == 0 or grid[new_rx][new_ry] == 0:
            # wall
            return (False, pushed_objects)
        elif (cx, cy) == (rx, ry):
            if grid[new_cx][new_cy] == 2:
                continue
            elif grid[new_cx][new_cy] == 1:
                q.add((new_cx, new_cy, new_rx, new_ry))
        else:
            if instruction == '<':
                if grid[new_cx][new_cy] == 2:
                    continue
                else:
                    q.add((new_cx, new_cy-1, new_cx, new_cy))
            elif instruction == '>':
                if grid[new_rx][new_ry] == 2:
                    continue
                else:
                    q.add((new_cx, new_ry, new_cx, new_ry+1))
            elif instruction in ('^', 'v'):
                if grid[new_cx][new_cy] == 2 and grid[new_rx][new_ry] == 2:
                    continue
                elif grid[new_cx][new_cy] == 4:
                    q.add((new_cx, new_cy, new_rx, new_ry))
                else:
                    if grid[new_cx][new_cy] == 5:
                        q.add((new_cx, new_cy-1, new_cx, new_cy))
                    if grid[new_rx][new_ry] == 4:
                        q.add((new_cx, new_ry, new_cx, new_ry+1))

    return (True, pushed_objects)

    
def process_instruction(grid, instruction, cx, cy):
    dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
    instruction_idx = [idx for idx, v in enumerate(['v', '^', '<', '>']) if v == instruction][0]
    x_delta, y_delta = dx[instruction_idx], dy[instruction_idx]
    nx, ny = cx + x_delta, cy + y_delta
    N, M = len(grid), len(grid[0])
    
    import copy
    grid = copy.deepcopy(grid)

    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        # no movement
        return (grid, cx, cy)
    elif grid[nx][ny] == 0:
        # it's a wall - no movement
        return (grid, cx, cy)
    elif grid[nx][ny] == 2:
        # it's a free space - move into it
        return (grid, nx, ny)
    elif grid[nx][ny] in (1, 4, 5):
        # look to see if we can push the barrels
        if grid[nx][ny] == 1:
            initial_object = (nx, ny, nx, ny)
        if grid[nx][ny] == 4:
            initial_object = (nx, ny, nx, ny+1)
        if grid[nx][ny] == 5:
            initial_object = (nx, ny-1, nx, ny)
        
        is_push_possible_flag, pushed_objs = move_objects(grid, initial_object, instruction)
        if is_push_possible_flag is True:
            for obj in pushed_objs:
                lx, ly, rx, ry = obj
                grid[lx][ly] = 2
                grid[rx][ry] = 2
            for obj in pushed_objs:
                lx, ly, rx, ry = obj
                if (lx, ly) == (rx, ry):
                    grid[lx + x_delta][ly+y_delta] = 1
                else:
                    grid[lx + x_delta][ly + y_delta] = 4
                    grid[rx + x_delta][ry + y_delta] = 5
            return (grid, nx, ny)
        else:
            return (grid, cx, cy)
        
    else:
        pass

    return None

def print_grid(grid, nx, ny):
    for i, row in enumerate(grid):
        x = ""
        for j, v in enumerate(row):
            if (i, j) == (nx, ny):
                x += '@'
            elif v == 0:
                x += '#'
            elif v == 1:
                x += 'O'
            elif v == 2:
                x += '.'
            elif v == 4:
                x += '['
            elif v == 5:
                x += ']'
            else:
                pass
        print(x)

for idx, instruction in enumerate(instructions):
    grid, cx, cy = process_instruction(grid, instruction, cx, cy)
    
tot = 0
for i, row in enumerate(grid):
    for j, _ in enumerate(row):
        tot += (100 * i + j) if grid[i][j] == 1 else 0
print(tot)

### PART TWO
new_grid = []

for _, row in enumerate(start_grid):
    x = []
    for _, v in enumerate(row):
        if v == 0:
            x += [0, 0]
        elif v == 1:
            x += [4, 5]
        elif v == 2:
            x += [2, 2]
        else:
            x += [3, 2]
    new_grid.append(x)

grid = new_grid

cx, cy = None, None
for i, row in enumerate(grid):
    for j, _ in enumerate(row):
        if grid[i][j] == 3:
            cx, cy = i, j
            grid[i][j] = 2

num_instructions = len(instructions)
for idx, instruction in enumerate(instructions):
    grid, cx, cy = process_instruction(grid, instruction, cx, cy)

tot = 0
for i, row in enumerate(grid):
    for j, _ in enumerate(row):
        tot += (100 * i + j) if grid[i][j] == 4 else 0
print(tot)