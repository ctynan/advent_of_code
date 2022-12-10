INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2021/inputs"
input_path = f"{INPUT_PREFIX}/day_10.txt"

CHAR_VALS = {')': 3, ']': 57, '}' : 1197, '>' : 25137}

def is_opener(x):
    if x in ['[', '(', '{', '<']:
        return True
    return False

def match(x, y):
    if x == '(':
        return y == ')'
    if x == '[':
        return y == ']'
    if x == '<':
        return y == '>'
    if x == '{':
        return y == '}'

### PART ONE
openers = []
score = 0
f_in = open(input_path)
while True:
    try:
        line = next(f_in).strip()
    except StopIteration:
        break

    for v in line:
        if is_opener(v):
            openers.append(v)
        else:
            item = openers.pop()
            if match(item, v) is True:
                continue
            else:
                score += CHAR_VALS[v]
                break

print(score)

### PART TWO
scores = []
f_in = open(input_path)
CHAR_VALS = {'(': 1, '[': 2, '{' : 3, '<' : 4}
while True:
    try:
        line = next(f_in).strip()
    except StopIteration:
        break
    corrupted_line = False
    openers = []
    for v in line:
        if is_opener(v):
            openers.append(v)
        else:
            item = openers.pop()
            if match(item, v) is True:
                continue
            else:
                corrupted_line = True
                break
    if corrupted_line is False:
        line_score = 0
        openers = reversed(openers)
        for v in openers:
            line_score *= 5
            line_score += CHAR_VALS[v]
        scores.append(line_score)

import statistics
print(statistics.median(scores))