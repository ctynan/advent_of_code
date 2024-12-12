INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2024/inputs"
input_path = f"{INPUT_PREFIX}/day_12.txt"

f_in = open(input_path)
grid = []
for line in f_in.readlines():
    line = line.strip()
    grid.append(line)

N, M = len(grid), len(grid[0])

def get_region_points(grid, x, y):
    region_points = set()
    N, M = len(grid), len(grid[0])
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    q = [(x,y)]
    while len(q) > 0:
        cx, cy = q.pop()
        region_points.add((cx,cy))
        for idx in range(4):
            nx, ny = cx + dx[idx], cy + dy[idx]
            if nx >= 0 and nx < N and ny >= 0 and ny < M:
                if grid[nx][ny] == grid[cx][cy] and (nx, ny) not in region_points:
                    q.append((nx,ny))
                else:
                    pass
            else:
                pass
    
    return region_points

def get_area_perimeter_sides(region_points, grid):
    N, M = len(grid), len(grid[0])
    area = len(region_points)
    perimeter_edges = set()
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    
    for v in region_points:
        x, y = v
        px, py = x*2, y*2
        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]
            if (nx, ny) not in region_points:
                perimeter_edges.add((px + dx[idx], py+dy[idx], idx))
            else:
                pass
    
    perimeter = len(perimeter_edges)
    sides = 0
    print("permieter edges: ", perimeter_edges)

    while len(perimeter_edges) > 0:
        px, py, edge_idx = perimeter_edges.pop()
        sides += 1
        removal_edges = set()
        removal_edges.add((px, py, edge_idx))
        while len(removal_edges) > 0:
            cx, cy, edge_idx = removal_edges.pop()
            if cx % 2 == 0:
                nx, ny = cx - 2, cy
                if (nx, ny, edge_idx) in perimeter_edges:
                    perimeter_edges.remove((nx,ny, edge_idx))
                    removal_edges.add((nx, ny, edge_idx))
                nx, ny = cx + 2, cy
                if (nx, ny, edge_idx) in perimeter_edges:
                    perimeter_edges.remove((nx,ny, edge_idx))
                    removal_edges.add((nx, ny, edge_idx))
            elif cy % 2 == 0:
                nx, ny = cx, cy + 2
                if (nx, ny, edge_idx) in perimeter_edges:
                    perimeter_edges.remove((nx,ny, edge_idx))
                    removal_edges.add((nx, ny, edge_idx))
                nx, ny = cx, cy - 2
                if (nx, ny, edge_idx) in perimeter_edges:
                    perimeter_edges.remove((nx,ny, edge_idx))
                    removal_edges.add((nx, ny, edge_idx))
            else:
                pass
    
    return area, perimeter, sides

visited_points = set()
price = 0
price_sides = 0

for i in range(N):
    for j in range(M):
        if (i, j) not in visited_points:
            region_points = get_region_points(grid, i, j)
            area, perimeter, sides = get_area_perimeter_sides(region_points, grid)
            
            visited_points = visited_points.union(region_points)
            price += area * perimeter
            price_sides += area * sides

print(price, price_sides)