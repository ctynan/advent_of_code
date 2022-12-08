INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2022/inputs"
INPUT_FILE = "day_07.txt"
input_path = f"{INPUT_PREFIX}/{INPUT_FILE}"

### READ IN AND PREPROCESS
f_in = open(input_path, 'r')
fs = dict()

_ = next(f_in)
cur_key = ["root"]
fs["root"] = dict()

def get_element(fs, cur_key):
    cur_element = fs
    for v in cur_key:
        cur_element = cur_element[v]
    return cur_element

CACHE = {}

def get_directory_sizes(fs, dir_name=""):
    tot = 0
    if dir_name in CACHE:
        return CACHE[dir_name]
    
    for k, v in fs.items():
        if type(v) == int:
            tot += v
        elif type(v) == dict:
            tot += get_directory_sizes(v, dir_name=dir_name+"/"+k)
    
    CACHE[dir_name] = tot
    return tot

while True:
    try:
        instruction = next(f_in).strip()
    except StopIteration:
        break
    if instruction == "$ ls":
        pass
    
    elif instruction.startswith("$ cd"):
        if instruction == "$ cd ..":
            cur_key = cur_key[:-1]
        else:
            new_folder = instruction.split()[-1]
            cur_key.append(new_folder)
    
    elif instruction.startswith("dir"):
        new_folder = instruction.split()[-1]
        cur_element = get_element(fs, cur_key)
        cur_element.setdefault(new_folder, dict())
    
    else:
        file_size, file_name = instruction.split()
        file_size = int(file_size)
        cur_element = get_element(fs, cur_key)
        cur_element[file_name] = file_size

    pass

get_directory_sizes(fs)

# PART ONE
print(sum([v for v in CACHE.values() if v <= 100000]))

# PART TWO
tot_used_space = CACHE["/root"]
rem_space = 70000000 - tot_used_space
print(min([v for v in CACHE.values() if rem_space + v >= 30000000]))


