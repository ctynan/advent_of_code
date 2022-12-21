INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2022/inputs"
input_path = f"{INPUT_PREFIX}/day_21.txt"

def solve(humn=None):
    global input_path
    f_in = open(input_path, 'r')
    known_vals = dict()
    opers = dict()

    while True:
        try:
            line = next(f_in).strip().replace(':', '').split()
            if len(line) == 2:
                known_vals[line[0]] = int(line[1])
            else:
                opers[line[0]] = (line[1], line[3], line[2])
        except StopIteration:
            break
    
    if humn is not None:
        known_vals['humn'] = humn
        opers['root'] = (opers['root'][0], opers['root'][1], '/')
    
    while True:
        if 'root' in known_vals:
            break
        keys_to_remove = set()
        for k, oper in opers.items():
            x, y, op = oper
            if x in known_vals and y in known_vals:
                a, b, = known_vals[x], known_vals[y]
                if op == '+':
                    val = a + b
                elif op == '-':
                    val = a - b
                elif op == '*':
                    val = a * b
                elif op == '/':
                    val = a / b
                known_vals[k] = val
                keys_to_remove.add(k)
            else:
                pass
        for k in keys_to_remove:
            del opers[k]

    print(humn, known_vals['root'])
    return known_vals['root']

### PART ONE
solve()

### PART TWO
lo, hi = 1, 17592186044416 # return function is monotonically decreasing, found manually
cur = (hi+lo) // 2
while True:
    ret = solve(cur)
    if abs(ret - 1) < 1e-15:
        break
    elif ret < 1:
        hi = cur
    elif ret > 1:
        lo = cur
    cur = (hi+lo) // 2

for j in range(cur - 10, cur + 10):
    print(j, solve(j))
