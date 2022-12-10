INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2021/inputs"
input_path = f"{INPUT_PREFIX}/day_12.txt"

f_in = open(input_path)
neighbours = dict()
CACHE = dict()

while True:
    try:
        line = next(f_in).strip()
    except StopIteration:
        break
    start, end = line.split('-')
    c_nodes = neighbours.setdefault(start, set())
    c_nodes.add(end)
    neighbours[start] = c_nodes

    c_nodes = neighbours.setdefault(end, set())
    c_nodes.add(start)
    neighbours[end] = c_nodes

### PART ONE
init_visited_nodes = set()
init_visited_nodes.add("start")
paths = [("start", init_visited_nodes)]
tot = 0

while len(paths) > 0:
    cur_node, visited_nodes = paths.pop(0)
    if cur_node == "end":
        tot += 1
        continue
    for next_node in neighbours[cur_node]:
        if next_node in visited_nodes and next_node.islower() is True:
            continue
        else:
            new_visited_nodes = set()
            new_visited_nodes = new_visited_nodes.union(visited_nodes)
            new_visited_nodes.add(next_node)
            paths.append((next_node, new_visited_nodes))

print(tot)

### PART TWO
visited_node_count = dict()
for node in neighbours:
    visited_node_count[node] = 0

visited_node_count["start"] = 1
paths = [("start", visited_node_count)]
tot = 0

while len(paths) > 0:
    cur_node, visited_nodes = paths.pop(0)
    if cur_node == "end":
        tot += 1
        continue
    for next_node in neighbours[cur_node]:
        if next_node.islower() is True:
            if next_node == "start":
                continue
            elif next_node == "end":
                paths.append((next_node, visited_nodes))
                continue
            else:
                import copy
                new_visited_nodes = copy.deepcopy(visited_nodes)
                visited_small_cave_twice = False
                for k, v in visited_nodes.items():
                    if k not in ("start", "end") and k.islower() is True and v >= 2:
                        visited_small_cave_twice = True
                if visited_small_cave_twice is False and visited_nodes[next_node] < 2:
                    new_visited_nodes[next_node] = visited_nodes[next_node] + 1
                    paths.append((next_node, new_visited_nodes))
                elif visited_small_cave_twice is True and visited_nodes[next_node] < 1:
                    new_visited_nodes[next_node] = visited_nodes[next_node] + 1
                    paths.append((next_node, new_visited_nodes))
                else:
                    continue
        else:
            paths.append((next_node, visited_nodes))

print(tot)