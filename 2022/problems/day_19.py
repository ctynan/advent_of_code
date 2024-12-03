INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2022/inputs"
input_path = f"{INPUT_PREFIX}/day_19.txt"

f_in = open(input_path, 'r')
blueprints = []

while True:
    try:
        _, line = next(f_in).strip().split(':')
        line = line.split('.')
        line = list(map(lambda x : x.strip().split(), line))
        costs = list(range(4))
        costs[0], costs[1] = int(line[0][-2]), int(line[1][-2])
        costs[2] = (int(line[2][-5]), int(line[2][-2]))
        costs[3] = (int(line[3][-5]), int(line[3][-2]))
        blueprints.append(costs)
    except StopIteration:
        break

def build(cur_resources : list, cur_robots : list, cur_focus_idx : int, blueprint : list, T : int, hist_res: list, hist_rob: list):
    if T == 24:
        return cur_resources[3]
    # Do we have the resources
    have_resources = True    
    if cur_focus_idx in (0, 1):
        if cur_resources[0] < blueprint[cur_focus_idx]:
            have_resources = False
    elif cur_focus_idx == 2:
        if cur_resources[0] < blueprint[2][0] or cur_resources[1] < blueprint[2][1]:
            have_resources = False
    elif cur_focus_idx == 3:
        if cur_resources[0] < blueprint[3][0] or cur_resources[2] < blueprint[3][1]:
            have_resources = False
    else:
        raise Exception
    import copy
    cur_resources = copy.deepcopy(cur_resources)
    cur_robots = copy.deepcopy(cur_robots)

    new_resources = list(map(lambda x, y: x + y, cur_resources, cur_robots))
    if have_resources is False:
        return build(new_resources, cur_robots, cur_focus_idx, blueprint, T+1, hist_res + [new_resources], hist_rob + [cur_robots])
    
    # So we do have the resources therefore we will build
    if cur_focus_idx == 0:
        new_resources[0] -= blueprint[0]
        cur_robots[0] += 1
        option_A = build(new_resources, cur_robots, 0, blueprint, T+1, hist_res + [new_resources], hist_rob + [cur_robots])
        option_B = build(new_resources, cur_robots, 1, blueprint, T+1, hist_res + [new_resources], hist_rob + [cur_robots])
        return max(option_A, option_B)
    elif cur_focus_idx == 1:
        new_resources[0] -= blueprint[1]
        cur_robots[1] += 1
        option_A = build(new_resources, cur_robots, 1, blueprint, T+1, hist_res + [new_resources], hist_rob + [cur_robots])
        option_B = build(new_resources, cur_robots, 2, blueprint, T+1, hist_res + [new_resources], hist_rob + [cur_robots])
        option_C = build(new_resources, cur_robots, 0, blueprint, T+1, hist_res + [new_resources], hist_rob + [cur_robots])
        return max([option_A, option_B, option_C])
    elif cur_focus_idx == 2:
        new_resources[0] -= blueprint[2][0]
        new_resources[1] -= blueprint[2][1]
        cur_robots[2] += 1
        option_A = build(new_resources, cur_robots, 2, blueprint, T+1, hist_res + [new_resources], hist_rob + [cur_robots])
        option_B = build(new_resources, cur_robots, 3, blueprint, T+1, hist_res + [new_resources], hist_rob + [cur_robots])
        option_C = build(new_resources, cur_robots, 1, blueprint, T+1, hist_res + [new_resources], hist_rob + [cur_robots])
        option_D = build(new_resources, cur_robots, 0, blueprint, T+1, hist_res + [new_resources], hist_rob + [cur_robots])
        return max([option_A, option_B, option_C, option_D])
    elif cur_focus_idx == 3:
        new_resources[0] -= blueprint[3][0]
        new_resources[2] -= blueprint[3][1]
        cur_robots[3] += 1
        return build(new_resources, cur_robots, 3, blueprint, T+1, hist_res + [new_resources], hist_rob + [cur_robots])
    else:
        raise Exception


for bp in blueprints:
    init_resources = [0, 0, 0, 0]
    init_robots = [1, 0, 0, 0]
    x = build(init_resources, init_robots, 0, bp, 0, [init_resources], [init_robots])
    y = build(init_resources, init_robots, 1, bp, 0, [init_resources], [init_robots])
    print(max(x,y))
