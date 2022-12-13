INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2022/inputs"
input_path = f"{INPUT_PREFIX}/day_13.txt"

import functools

def preprocess(x):
    from ast import literal_eval
    x = literal_eval(x)
    return x

def comp(x, y):
    import copy
    nx = copy.deepcopy(x)
    ny = copy.deepcopy(y)
    x = nx
    y = ny
    if len(x) == 0 or len(y) == 0:
        if len(x) == 0:
            if len(y) == 0:
                return 0
            else:
                return -1
        elif len(y) == 0:
            if len(x) == 0:
                return 0
            else:
                return 1
    
    if int(type(x[0])==int) + int(type(y[0])==int) == 1:
        x[0] = [x[0]] if type(x[0]) is int else x[0]
        y[0] = [y[0]] if type(y[0]) is int else y[0]
        return comp(x,y)
    
    if type(x[0]) is int and type(y[0]) is int:
        if x[0] < y[0]:
            return -1
        elif x[0] == y[0]:
            if len(x) == 1 and len(y) == 1:
                return 0
            else:
                return comp(x[1:], y[1:])
        else:
            return 1

    elif type(x[0]) is list and type(y[0]) is list:
        if comp(x[0], y[0]) == 0:
            nx, ny = x[1:], y[1:]
            if len(x) == 1:
                nx = []
            if len(y) == 1:
                ny = []
            return comp(nx, ny)
        else:
            return comp(x[0], y[0])
        
    raise Exception

### PART ONE
f_in = open(input_path, 'r')
tot = 0
idx = 1
while True:
    x = next(f_in).strip()
    y = next(f_in).strip()
    x = preprocess(x)
    y = preprocess(y)
    if comp(x,y) < 0:
        tot += idx
    try: 
        _ = next(f_in)
        idx += 1
    except StopIteration:
        break

print(tot)

### PART TWO
f_in = open(input_path, 'r')
rows = [[[2]], [[6]]]

while True:
    x = next(f_in).strip()
    y = next(f_in).strip()
    x = preprocess(x)
    y = preprocess(y)
    rows.append(x)
    rows.append(y)
    try: 
        _ = next(f_in)
    except StopIteration:
        break

rows = sorted(rows, key=functools.cmp_to_key(comp))
ret = 1
for idx, v in enumerate(rows):
    if v == [[2]]:
        ret *= (idx+1)
    elif v == [[6]]:
        ret *= (idx+1)
    else:
        pass

print(ret)