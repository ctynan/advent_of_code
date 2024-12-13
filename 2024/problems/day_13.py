INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2024/inputs"
input_path = f"{INPUT_PREFIX}/day_13.txt"

f_in = open(input_path)
button_A, button_B, prize = [], [], []

for line in f_in.readlines():
    line = line.strip()
    if line[:9] == 'Button A:':
        line = line.replace('Button A: X+', '').replace(', Y+', ' ')
        lv = list(map(int,line.split()))
        button_A.append((lv[0], lv[1]))
    if line[:9] == 'Button B:':
        line = line.replace('Button B: X+', '').replace(', Y+', ' ')
        lv = list(map(int,line.split()))
        button_B.append((lv[0], lv[1]))
    if line[:6] == 'Prize:':
        line = line.replace('Prize: X=', '').replace(', Y=', ' ')
        lv = list(map(int,line.split()))
        prize.append((lv[0], lv[1]))

### PART ONE
tot = 0
for idx, v in enumerate(prize):
    px, py = v
    best = None
    for i in range(101):
        for j in range(101):
            ax, ay = button_A[idx]
            bx, by = button_B[idx]
            if ax*i + bx*j == px and ay*i + by*j == py:
                cost = 3*i + j
                if best is None or cost < best:
                    best = cost
    tot += 0 if best is None else cost

print(tot)

### PART TWO
tot = 0
for idx, v in enumerate(prize):
    px, py = v
    px += 10000000000000
    py += 10000000000000
    ax, ay = button_A[idx]
    bx, by = button_B[idx]
    cost = None
    if by * px - bx * py == 0 and ay * px - ax * py == 0:
        cost = min(3 * px // ax, py // by)
    elif by * px - bx * py == 0:
        cost = py // by
    elif ay * px - ax * py == 0:
        cost = 3 * px // ax
    else:
        numerator = by*px - py*bx
        denominator = ax*by - ay*bx
        if numerator % denominator == 0:
            i = numerator // denominator
            if (px - ax*i) % bx == 0:
                j = (px - ax*i) // bx
                if i >= 0 and j >= 0:
                    cost = 3*i + j
    tot += 0 if cost is None else cost

print(tot)
