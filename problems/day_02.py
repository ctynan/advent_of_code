INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/problems/inputs"
input_path = f"{INPUT_PREFIX}/day_02.txt"
f_in = open(input_path)

def outcome_score(op, you):
    if op == 'A':
        if you == 'X':
            return 3
        elif you == 'Y':
            return 6
        else:
            return 0
    if op == 'B':
        if you == 'Y':
            return 3
        elif you =='Z':
            return 6
        else:
            return 0
    if op == 'C':
        if you == 'Z':
            return 3
        elif you == 'X':
            return 6
        else:
            return 0
    raise Exception

def your_value(you):
    return 1 + ord(you) - ord('X')

### PART ONE
tot = 0
for line in f_in.readlines():
    op, you = line.strip().split()
    tot += outcome_score(op, you) + your_value(you)

print(tot)

def your_move(op, outcome):
    poss_moves = ['X', 'Y', 'Z']
    desired_points = {'X' : 0, 'Y' : 3, 'Z' : 6}
    for move in poss_moves:
        if outcome_score(op, move) == desired_points[outcome]:
            return move
    raise Exception

### PART TWO
f_in = open(input_path)
tot = 0
for line in f_in.readlines():
    op, outcome = line.strip().split()
    you = your_move(op, outcome)
    tot += outcome_score(op, you) + your_value(you)

print(tot)