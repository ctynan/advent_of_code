INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2022/inputs"
input_path = f"{INPUT_PREFIX}/day_11.txt"

f_in = open(input_path, 'r')

monkey_items = []
operations = []
divisibilties = []
next_monkey_true = []
next_monkey_false = []

while True:
    _ = next(f_in)
    starting_items = next(f_in).strip()
    starting_items = starting_items.replace('Starting items:', '')
    monkey_items.append(list(map(int,starting_items.strip().split(','))))
    operation = next(f_in).strip()
    operations.append(operation.split()[-3:])
    divisibilty_rule = next(f_in).strip()
    divisibilties.append(int(divisibilty_rule.split()[-1]))
    next_if_true = next(f_in).strip()
    next_monkey_true.append(int(next_if_true.split()[-1]))
    next_if_false = next(f_in).strip()
    next_monkey_false.append(int(next_if_false.split()[-1]))
    
    try:
        _ = next(f_in)
    except StopIteration:
        break

def calc_new_value(x, operation, divisor):
    operand = operation[1]
    left = x if operation[0] == "old" else int(operation[0])
    right = x if operation[2] == "old" else int(operation[2])
    if operand == '+':
        ret = left + right
    elif operand == '-':
        ret = left - right
    elif operand == '*':
        ret = left * right
    elif operand == '/':
        ret = left / right
    return ret // divisor

import copy
monkey_items_copy = copy.deepcopy(monkey_items)
### PART ONE
tots = [0 for _ in range(len(monkey_items))]
for t in range(20):
    for idx, v in enumerate(monkey_items):
        tots[idx] += len(v)
        for monkey_item in v:
            new_item_value = calc_new_value(monkey_item, operations[idx], divisor=3)
            test_flag = (new_item_value % divisibilties[idx] == 0)
            if test_flag is True:
                monkey_items[next_monkey_true[idx]].append(new_item_value)
            else:
                monkey_items[next_monkey_false[idx]].append(new_item_value)
        monkey_items[idx] = []

tots = sorted(tots, reverse=True)
print(tots[0]*tots[1])

### PART TWO
import math
MOD_FACTOR = math.prod(divisibilties)
tots = [0 for _ in range(len(monkey_items))]
for t in range(10000):
    for idx, v in enumerate(monkey_items_copy):
        tots[idx] += len(v)
        for monkey_item in v:
            new_item_value = calc_new_value(monkey_item, operations[idx], divisor=1)
            new_item_value = new_item_value % MOD_FACTOR
            assert new_item_value >= 0
            assert new_item_value < MOD_FACTOR
            test_flag = (new_item_value % divisibilties[idx] == 0)
            if test_flag is True:
                monkey_items_copy[next_monkey_true[idx]].append(new_item_value)
            else:
                monkey_items_copy[next_monkey_false[idx]].append(new_item_value)
        monkey_items_copy[idx] = []

tots = sorted(tots, reverse=True)
print(tots[0]*tots[1])