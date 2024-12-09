INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2024/inputs"
input_path = f"{INPUT_PREFIX}/day_09.txt"

f_in = open(input_path)

for line in f_in.readlines():
    line = line.strip()

blocks = []
for idx, v in enumerate(line):
    v = int(v)
    if idx % 2 == 0:
        file_idx = idx // 2
        for _ in range(v):
            blocks.append(file_idx)
    else:
        for _ in range(v):
            blocks.append(-1)

### PART ONE
def move_blocks(blocks):
    import copy 
    blocks = copy.deepcopy(blocks)
    cursor_idx = len(blocks) - 1
    for idx, v in enumerate(blocks):
        if v == -1:
            while True:
                if idx >= cursor_idx:
                    return blocks
                elif blocks[cursor_idx] >= 0:
                    blocks[idx] = blocks[cursor_idx]
                    blocks[cursor_idx] = -1
                    cursor_idx -= 1
                    break
                else:
                    cursor_idx -= 1
        else:
            continue
    
    return blocks

moved_blocks = move_blocks(blocks)
checksum = sum([idx * v for idx, v in enumerate(moved_blocks) if v >= 0])

print(checksum)

### PART TWO
N = len(blocks)
max_idx = max(blocks) + 1
for idx in range(N):
    cur_idx = N - 1 - idx
    block_idx = blocks[cur_idx]
    if block_idx >= 0 and block_idx < max_idx:
        max_idx = block_idx
        while cur_idx >= 0 and blocks[cur_idx] == block_idx:
            cur_idx -= 1
        block_length = (N - 1 - idx) - cur_idx
        for j in range(N):
            if j > cur_idx:
                break
            else:
                if max(blocks[j:j+block_length]) == -1:
                    for k in range(block_length):
                        blocks[j+k] = block_idx
                        blocks[cur_idx + 1 + k] = -1
                    break
                else:
                    pass

checksum = sum([idx * v for idx, v in enumerate(blocks) if v >= 0])
print(checksum)