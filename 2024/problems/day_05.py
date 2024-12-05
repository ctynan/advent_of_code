import os
INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2024/inputs"
input_path = f"{INPUT_PREFIX}/day_05.txt"

f_in = open(input_path)
rules = {}
updates = []

for line in f_in.readlines():
    line = line.strip()
    if '|' in line:
        vals = list(map(int, line.split('|')))
        y, x = vals[0], vals[1]
        cv = rules.get(x, set())
        cv.add(y)
        rules[x] = cv
    elif ',' in line:
        updates.append(line)

### PART ONE
tot = 0

def is_update_ordered(rules, update):
    printed = set()
    for v in update:
        for z in rules.get(v, set()):
            if z not in printed and z in update:
                return False
        printed.add(v)
    return True

for update in updates:
    update = list(map(int,update.split(',')))
    if is_update_ordered(rules, update):
        tot += update[(len(update)-1) // 2]

print(tot)

### PART TWO
tot = 0

def order_update(rules, update, printed):
    for idx, v in enumerate(update):
        # Check if we can put this value at the front
        has_dependency = False
        for z in rules.get(v, set()):
            if z not in printed and z in update:
                has_dependency = True
                break
        if has_dependency is True:
            continue
        else:
            return order_update(rules, update[0:idx] + update[(idx+1):], printed + [v])
        
    return printed

for update in updates:
    update = list(map(int,update.split(',')))
    if is_update_ordered(rules, update) is False:
        ordered_update = order_update(rules, update, [])
        tot += ordered_update[(len(ordered_update)-1) // 2]

print(tot)