INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/problems/inputs"
INPUT_FILE = "day_05.txt"
input_path = f"{INPUT_PREFIX}/{INPUT_FILE}"

def move(piles, num_moves, from_pile, to_pile, reverse=True):
    if reverse is True:
        piles[to_pile] = list(reversed(piles[from_pile][:num_moves])) + piles[to_pile]
    else:
        piles[to_pile] = piles[from_pile][:num_moves] + piles[to_pile]
    
    piles[from_pile] = piles[from_pile][num_moves:]
    return piles

def solve(f_in, reverse=True):
    starting_lines = []
    while True:
        line = next(f_in)
        if line.strip().split()[0].isdigit() == True:
            num_piles = int(line.strip().split()[-1])
            break
        else:
            starting_lines.append(line)

    _ = next(f_in)
    piles = []
    for _ in range(num_piles):
        piles.append([])

    for line in starting_lines:
        line = line.strip('\n').replace('[', ' ').replace(']', ' ')
        for idx in range(num_piles):
            pile_char = line[4*idx + 1]
            if pile_char != ' ':
                piles[idx].append(pile_char)

    while True:
        try:
            line = next(f_in)
        except StopIteration:
            break
        lv = line.strip('\n').split()
        num_moves, from_pile, to_pile = int(lv[1]), int(lv[3]) - 1, int(lv[5]) - 1
        piles = move(piles, num_moves, from_pile, to_pile, reverse=reverse)

    print(''.join(v[0] for v in piles))
    return

### PART ONE
f_in = open(input_path)
solve(f_in, reverse=True)

### PART TWO
f_in = open(input_path)
solve(f_in, reverse=False)
