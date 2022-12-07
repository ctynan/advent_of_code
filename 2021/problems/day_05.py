INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2021/inputs"
input_path = f"{INPUT_PREFIX}/day_05.txt"

f_in = open(input_path)

points = [[0 for _ in range(1000)] for __ in range(1000)]

while True:
    try:
        line = next(f_in)
    except StopIteration:
        break
    start_xy, end_xy = line.strip().split("->")
    start_x, start_y = list(map(int,start_xy.strip().split(',')))
    end_x, end_y = list(map(int, end_xy.strip().split(',')))
    if start_x == end_x:
        lo, hi = min(start_y, end_y), max(start_y, end_y)
        for j in range(lo, hi+1):
            points[start_x][j] += 1
    elif start_y == end_y:
        lo, hi = min(start_x, end_x), max(start_x, end_x)
        for j in range(lo, hi+1):
            points[j][start_y] += 1
    else:
        ### PART TWO logic
        diff = abs(start_x-end_x)
        x_sign = 1 if end_x > start_x else -1
        y_sign = 1 if end_y > start_y else -1
        for i in range(diff+1):
            nx, ny = start_x + (i * x_sign), start_y + (i * y_sign)
            points[nx][ny] += 1
        
ret = sum(len([v for v in row if v >= 2]) for row in points)
print(ret)