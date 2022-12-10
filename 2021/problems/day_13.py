INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2021/inputs"
input_path = f"{INPUT_PREFIX}/day_13.txt"

f_in = open(input_path)
points = set()
instructions = []
while True:
    try:
        line = next(f_in).strip()
        if line == "":
            continue
        elif line.startswith("fold"):
            instructions.append(line)
        else:
            y, x = int(line.split(',')[0]), int(line.split(',')[1])
            points.add((x, y))
    except StopIteration:
        break

def process_instruction(points, instruction):
    fold_line = instruction.strip().split()[-1]
    dim, val = fold_line.split('=')[0], int(fold_line.split('=')[1])
    new_points = set()
    for v in points:
        cx, cy = v
        if dim == 'y':
            if cx < val:
                new_points.add((cx,cy))
            else:
                nx = val - (cx-val)
                ny = cy
                new_points.add((nx,ny))
        elif dim == 'x':
            if cy < val:
                new_points.add((cx,cy))
            else:
                ny = val - (cy-val)
                nx = cx
                new_points.add((nx,ny))
    return new_points

### PARTS ONE AND TWO            
print(len(points))
for inst in instructions:
    points = process_instruction(points, inst)
    print(len(points))

max_x = max([v[0] for v in points])+1
max_y = max([v[1] for v in points])+1
grid = []
for _ in range(max_x):
    row = ['.' for _ in range(max_y)]
    grid.append(row)
for v in points:
    x, y = v
    grid[x][y] = '#'

for row in grid:
    print(row)
