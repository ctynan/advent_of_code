INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2021/inputs"
input_path = f"{INPUT_PREFIX}/day_03.txt"

### PART ONE
f_in = open(input_path)
lines = []
while True:
    try:
        line = next(f_in).strip()
        lines.append(line)
    except StopIteration:
        break

n, m = len(lines), len(lines[0])
gamma = []

for j in range(m):
    cnt = 0
    for i in range(n):
        cnt += int(lines[i][j])
    if 2 * cnt > n:
        gamma.append(1)
    else:
        gamma.append(0)

gamma = list(reversed(gamma))
gamma_rate = sum([v * 2**idx for idx, v in enumerate(gamma)])
epsilon_rate = sum([((v+1) % 2) * 2**idx for idx, v in enumerate(gamma)])

print(gamma_rate, epsilon_rate, gamma_rate*epsilon_rate)

### PART TWO
def filter_values(values, idx=0, use_most=True):
    if len(values) == 1:
        return values[0]
    
    n = len(values)
    tot = sum([int(v[idx]) for v in values])
    to_keep = None
    if 2 * tot >= n:
        to_keep = 1
    else:
        to_keep = 0
    if use_most is False:
        to_keep = (to_keep + 1) % 2
    
    new_values = [v for v in values if int(v[idx]) == to_keep]
    
    return filter_values(new_values, idx+1, use_most)    

oxygen_value = filter_values(lines, idx=0, use_most=True)
co2_value = filter_values(lines, idx=0, use_most=False)

oxygen_value = list(reversed(oxygen_value))
co2_value = list(reversed(co2_value))

oxygen_rate = sum([int(v) * 2**idx for idx, v in enumerate(oxygen_value)])
co2_rate = sum([int(v) * 2**idx for idx, v in enumerate(co2_value)])

print(oxygen_rate, co2_rate, oxygen_rate*co2_rate)