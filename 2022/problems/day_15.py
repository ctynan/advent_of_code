INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2022/inputs"
input_path = f"{INPUT_PREFIX}/day_15.txt"

f_in = open(input_path)
sensors, beacons = [], []

while True:
    try:
        line = next(f_in).strip()
        line = line.replace(',','').replace(':', '').replace('=',' ')
        lv = line.split()
        sensor_x, sensor_y = int(lv[3]), int(lv[5])
        beacon_x, beacon_y = int(lv[-3]), int(lv[-1])
        sensors.append((sensor_x, sensor_y))
        beacons.append((beacon_x, beacon_y))
    except StopIteration:
        break

def no_beacon_x_segments(sensors, beacons, y):
    segments = []
    for idx, sensor in enumerate(sensors):
        beacon = beacons[idx]
        sx, sy = sensor
        bx, by = beacon
        mh_dist = abs(sx-bx) + abs(sy-by)
        y_dist = abs(y-sy)
        if y_dist >= mh_dist:
            continue
        else:
            rem_dist = mh_dist - y_dist
            segments.append(((sx - rem_dist), (sx + rem_dist)))
    return segments

### PART ONE
Y = 2000000
segs = no_beacon_x_segments(sensors=sensors, beacons=beacons, y=Y)
segs = sorted(segs, key=lambda x : (x[0], x[1]))

def merge_segments(segments):
    if len(segments) == 1:
        return segments
    else:
        new_segments = []
        cx, cy = segments[0]
        nx, ny = segments[1]
        if nx > cy:
            if nx == cy + 1:
                new_segments.append((cx, ny))
                if len(segments) == 2:
                    return new_segments
                else:
                    return merge_segments(new_segments + segments[2:])
            else:
                # No overlap
                new_segments.append((cx, cy))
                return new_segments + merge_segments(segments[1:])
        else:
            new_segments.append((cx, max(cy,ny)))
            if len(segments) == 2:
                return new_segments
            else:
                return merge_segments(new_segments + segments[2:])
        
ns = merge_segments(segs)
lo, hi = ns[0]
tot = hi - lo + 1
beacon_set = set()
for v in beacons:
    x, y = v
    beacon_set.add((x,y))
num_beacons = len([v for x, v in beacon_set if v == Y])
print(hi - lo + 1 - num_beacons)

### PART TWO
segs = no_beacon_x_segments(sensors=sensors, beacons=beacons, y=Y)
segs = sorted(segs, key=lambda x : (x[0], x[1]))

import time
ts = time.monotonic()
for y in range(4000001):
    if y % 100000 == 0:
        print(y, (time.monotonic()-ts))
    segs = no_beacon_x_segments(sensors=sensors, beacons=beacons, y=y)
    segs = sorted(segs, key=lambda x : (x[0], x[1]))
    ns = merge_segments(segs)
    if len(ns) == 2:
        _, x = ns[0]
        x += 1
        print((x,y))
