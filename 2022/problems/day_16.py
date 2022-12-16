INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2022/inputs"
input_path = f"{INPUT_PREFIX}/day_16.txt"

f_in = open(input_path, 'r')

nodes = set()
edges = dict()
flows = dict()

while True:
    try:
        line = next(f_in).strip()
        line = line.replace(',', '')
        lv = line.split(';')
        cur_node = lv[0].split()[1]
        nodes.add(cur_node)
        flows[cur_node] = int(lv[0].split('=')[1])
        edges[cur_node] = set([v for v in lv[1].split()[4:]])
    except StopIteration:
        break

### PART ONE

def get_shortest_path(start, end, edges):
    cur_node = start
    visited = set()
    visited.add(start)
    q = [(start, 0)]
    while len(q) > 0:
        cur_node, dist = q.pop(0)
        if cur_node == end:
            return dist
        for v in edges[cur_node]:
            if v in visited:
                continue
            else:
                q.append((v, dist+1))
                visited.add(v)
    raise Exception

dist = dict()
for start_node in nodes:
    for end_node in nodes:
        dist[(start_node,end_node)] = get_shortest_path(start_node, end_node, edges)

valves_to_open = [k for k, v in flows.items() if v > 0]
N = len(valves_to_open)
num_subsets = 2**(N)
T = 31

### want idx -> set mapping
valve_idx = dict()
for i, v in enumerate(valves_to_open):
    valve_idx[v] = i+1
valve_idx['AA'] = 0

idx_valve_set_dict = dict()
for i in range(num_subsets):
    valve_set = set()
    for j in range(N):
        if i & 2**j > 0:
            valve_set.add(valves_to_open[j])
    idx_valve_set_dict[i] = valve_set

cur_pressure_idx = dict()
for i in range(num_subsets):
    tot = 0 
    for j in range(N):
        if i & 2**j > 0:
            tot += flows[valves_to_open[j]]
    cur_pressure_idx[i] = tot

### set up recursion
dp = []
for i in range(num_subsets):
    dp.append([])
    for j in range(N+1):
        dp[i].append([-1 for _ in range(T)])

dp[0][0][0] = 0

def calc_new_idx(valve_set, valves_to_open, next_valve):
    tot = 0
    for i, v in enumerate(valves_to_open):
        if v in valve_set or v == next_valve:
            tot += 2**i
    return tot

valve_iteration_list = ['AA'] + valves_to_open 
for t in range(0,T):    
    for cur_valve in valve_iteration_list:
        cur_valve_idx = valve_idx[cur_valve]
        for idx in range(num_subsets):
            tot_pressure = dp[idx][cur_valve_idx][t]
            cur_pressure = cur_pressure_idx[idx]
            cur_open_valves = idx_valve_set_dict[idx]
            
            if tot_pressure >= 0:
                ### calc poss next valve
                for v in valves_to_open:
                    if v not in cur_open_valves:
                        ### could go here next
                        new_t = t + dist[(cur_valve, v)] + 1
                        new_total_pressure = tot_pressure + (new_t - t) * cur_pressure
                        if new_t < T:
                            new_valve_set_idx = calc_new_idx(cur_open_valves, valves_to_open, v)
                            new_valve_idx = valve_idx[v]
                            dp[new_valve_set_idx][new_valve_idx][new_t] = max(dp[new_valve_set_idx][new_valve_idx][new_t], new_total_pressure)
            ### can always just hang out somewhere
            if t > 0 and dp[idx][cur_valve_idx][t-1] >= 0:
                dp[idx][cur_valve_idx][t] = max(dp[idx][cur_valve_idx][t], dp[idx][cur_valve_idx][t-1]+cur_pressure)

best = -1
for idx in range(num_subsets):
    for j in range(N+1):
        tp = dp[idx][j][T-1]
        best = max(tp, best)
print(best)

### PART TWO

T = 27
best = -1
for idx in range(num_subsets):
    ### get the subset
    best_X = -1
    cur_open_valves = idx_valve_set_dict[idx]
    for j in range(N+1):
        best_X = max(dp[idx][j][T-1], best_X)
    
    rem_valves = set(valves_to_open).difference(cur_open_valves)
    poss_num_subsets = 2**len(rem_valves)
    for i in range(poss_num_subsets):
        new_subset = set()
        for j, v in enumerate(rem_valves):
            if i & 2**j > 0:
                new_subset.add(v)
        new_idx = calc_new_idx(new_subset, valves_to_open, None)
        best_Y = -1
        for j in range(N+1):
            best_Y = max(dp[new_idx][j][T-1], best_Y)
        best = max(best, best_X+best_Y)
print(best)


