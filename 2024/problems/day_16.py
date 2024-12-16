INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2024/inputs"
input_path = f"{INPUT_PREFIX}/day_16.txt"

f_in = open(input_path)
grid = []

for line in f_in.readlines():
    line = line.strip()
    grid.append(line)

start_x, start_y, goal_x, goal_y = None, None, None, None
for i, row in enumerate(grid):
    for j, v in enumerate(row):
        if grid[i][j] == 'S':
            start_x, start_y = i, j
        elif grid[i][j] == 'E':
            goal_x, goal_y = i, j
        else:
            continue
    grid[i] = grid[i].replace('E', '.').replace('S', '.')

import heapq
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
N, M = len(grid), len(grid[0])
visited_states = dict()
visited_states[(start_x, start_y, 0)] = 0
q = []
heapq.heappush(q, (0, (start_x, start_y, 0, [(start_x, start_y)])))
optimal_nodes = set()
optimal_cost = None

while len(q) > 0:
    cost, (cx, cy, dir_idx, visited_nodes) = heapq.heappop(q)
    visited_states[(cx, cy, dir_idx)] = cost
    
    if (cx, cy) == (goal_x, goal_y) and optimal_cost is None:
        print(f"Optimal cost is {cost}")
        optimal_cost = cost
    
    if optimal_cost is not None:
        if cost > optimal_cost:
            break
        elif (cx, cy) == (goal_x, goal_y):
            for v in visited_nodes:
                visit_x, visit_y = v
                optimal_nodes.add((visit_x, visit_y))
        else:
            pass
    
    # try moving forward
    nx, ny = cx + dx[dir_idx], cy + dy[dir_idx]
    if nx >= 0 and nx < N and ny >= 0 and ny < M:
        if grid[nx][ny] == '.':
            if (nx, ny, dir_idx) not in visited_states:
                heapq.heappush(q, (cost+1, (nx, ny, dir_idx, visited_nodes + [(nx, ny)])))
                visited_states[(nx, ny, dir_idx)] = cost + 1
            else:
                if cost + 1 <= visited_states[(nx, ny, dir_idx)]:
                    visited_states[(nx, ny, dir_idx)] = cost + 1
                    heapq.heappush(q, (cost+1, (nx, ny, dir_idx, visited_nodes + [(nx, ny)])))
        else:
            pass
    else:
        pass

    # change direction
    new_dir_idx = (dir_idx + 1) % 4
    nx, ny = cx, cy
    if (nx, ny, new_dir_idx) not in visited_states:
        heapq.heappush(q, (cost+1000, (nx, ny, new_dir_idx, visited_nodes + [(nx, ny)])))
        visited_states[(nx, ny, new_dir_idx)] = cost + 1000
    else:
        if cost + 1000 <= visited_states[(nx, ny, new_dir_idx)]:
            visited_states[(nx, ny, new_dir_idx)] = cost + 1000
            heapq.heappush(q, (cost+1000, (nx, ny, new_dir_idx, visited_nodes + [(nx, ny)])))
    
    new_dir_idx = (dir_idx + 3) % 4
    nx, ny = cx, cy
    if (nx, ny, new_dir_idx) not in visited_states:
        heapq.heappush(q, (cost+1000, (nx, ny, new_dir_idx, visited_nodes + [(nx, ny)])))
        visited_states[(nx, ny, new_dir_idx)] = cost + 1000
    else:
        if cost + 1000 <= visited_states[(nx, ny, new_dir_idx)]:
            visited_states[(nx, ny, new_dir_idx)] = cost + 1000
            heapq.heappush(q, (cost+1000, (nx, ny, new_dir_idx, visited_nodes + [(nx, ny)])))

print(len(optimal_nodes))