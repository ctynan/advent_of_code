INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2021/inputs"
input_path = f"{INPUT_PREFIX}/day_04.txt"

f_in = open(input_path)
order = list(map(int, next(f_in).split(',')))
_ = next(f_in)
boards = []

while True:
    input_rows = []
    try:
        for _ in range(5):
            new_row = list(map(int, next(f_in).strip().split()))
            assert len(new_row) == 5
            input_rows.append(new_row)
        boards.append(input_rows)
        _ = next(f_in)
    except StopIteration:
        break

import copy
marked = copy.deepcopy(boards)

def update_boards(boards, v):
    for board in boards:
        for i in range(5):
            for j in range(5):
                if board[i][j] == v:
                    board[i][j] = 0
    return boards

def exists_winning_board(boards):
    for board in boards:
        for i in range(5):
            if sum([v[i] for v in board]) == 0:
                return True, board
            elif sum(board[i]) == 0:
                return True, board
            else:
                continue
    return False, None

board_tot = 25*13
for idx, v in enumerate(order):
    boards = update_boards(boards, v)
    status, board = exists_winning_board(boards)
    if status is True:
        ret = v * sum([sum(v) for v in board])
        break
print(ret)

### PART TWO

def idx_board_wins(board, order):
    new_boards = [board]
    for idx, v in enumerate(order):
        new_boards = update_boards(new_boards, v)
        status, board = exists_winning_board(new_boards)
        if status is True:
            return idx, board, v

board_finishers = []
for b in marked:
    board_finishers.append(idx_board_wins(b, order))

from operator import itemgetter
board_finishers = sorted(board_finishers, key=itemgetter(0), reverse=True)
_, board, v = board_finishers[0]
ret = v * sum([sum(v) for v in board])
print(ret)
