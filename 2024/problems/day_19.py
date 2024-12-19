INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2024/inputs"
input_path = f"{INPUT_PREFIX}/day_19.txt"

f_in = open(input_path)
towels = []
tgts = []

for line in f_in.readlines():
    line = line.strip()
    if ',' in line:
        towels = line.split(',')
        towels = [v.strip() for v in towels]
    elif len(line.strip()) > 0:
        tgts.append(line)

def is_possible(tgt, towels):
    N = len(tgt)
    dp = [0 for _ in range(N+1)]
    dp[0] = 1

    for i in range(N+1):
        for j in range(i):
            if tgt[j:i] in towels:
                dp[i] += dp[j]
    
    return dp[N]

print(sum([1 for v in tgts if is_possible(v, towels) > 0]))
print(sum([is_possible(v, towels) for v in tgts ]))