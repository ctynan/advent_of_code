INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2022/inputs"
input_path = f"{INPUT_PREFIX}/day_10.txt"

f_in = open(input_path)
CYCLE_NUM, X, tot = 1, 1, 0

### PART ONE
while True:
    try:
        instruction = next(f_in).strip()
    except StopIteration:
        break
    if instruction == "noop":
        if CYCLE_NUM % 40 == 20 and CYCLE_NUM <= 220:
            tot += CYCLE_NUM*X
        CYCLE_NUM += 1
        
    else:
        delta = int(instruction.split()[1])
        for _ in range(2):
            if CYCLE_NUM % 40 == 20 and CYCLE_NUM <= 220:
                tot += CYCLE_NUM*X
            CYCLE_NUM += 1
        X += delta

print(tot)
    
### PART TWO
f_in = open(input_path)
CYCLE_NUM, X = 1, 1
grid = []
for _ in range(6):
    row = []
    for _ in range(40):
        row.append(".")
    grid.append(row)

while True:
    try:
        instruction = next(f_in).strip()
    except StopIteration:
        break
    if instruction == "noop":
        row_idx = (CYCLE_NUM-1) // 40
        col_idx = (CYCLE_NUM - 1) % 40 
        if abs(X-col_idx) <= 1:
            grid[row_idx][col_idx] = '#'
        CYCLE_NUM += 1
        
    else:
        delta = int(instruction.split()[1])
        for _ in range(2):
            row_idx = (CYCLE_NUM-1) // 40
            col_idx = (CYCLE_NUM - 1) % 40 
            if abs(X-col_idx) <= 1:
                grid[row_idx][col_idx] = '#'
            
            CYCLE_NUM += 1
        X += delta

for v in grid:
    print(v)    
