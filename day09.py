# Day 9: Movie Theater

import load_data as ld
import os
from collections import deque

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f"example{day}.txt")
data = ld.load_data(f"input{day}.txt")

red_tiles = []
for line in data:
    x, y = map(int, line.split(','))
    red_tiles.append((x, y))

max_area = 0

for i, tile in enumerate(red_tiles):
    ri, ci = tile
    for j, other_tile in enumerate(red_tiles):
        rj, cj = other_tile
        area = abs(ri - rj + 1) * abs(ci - cj + 1)
        if area > max_area:
            max_area = area

print(max_area)

# Part 2
green_tiles = []
for i in range(len(red_tiles)):
    xi, yi = red_tiles[i]
    xj, yj = red_tiles[i-1]
    if xi == xj:
        y_min = min(yi, yj)
        y_max = max(yi, yj)
        for y in range(y_min + 1, y_max):
            green_tiles.append((xi, y))
    elif yi == yj:
        x_min = min(xi, xj)
        x_max = max(xi, xj)
        for x in range(x_min + 1, x_max):
            green_tiles.append((x, yi))

# Fill in enclosed zones with green tiles

# Compare only valid areas

# Following along HyperNeutrino
points = [list(map(int, line.split(','))) for line in data]

xs = sorted({x for x, _ in points})
ys = sorted({y for _, y in points})

# x_sizes = {}
# y_sizes = {}

# for i, (x1, x2) in enumerate(zip(xs, xs[1:])):
#     x_sizes[i * 2 + 1] = x2 - x1 - 1

# for i, (y1, y2) in enumerate(zip(ys, ys[1:])):
#     y_sizes[i * 2 + 1] = y2 - y1 - 1

grid = [[0] * (len(ys) * 2 - 1) for _ in range(len(xs) * 2 - 1)]

for (x1, y1), (x2, y2) in zip(points, points[1:] + points[:1]):
    cx1, cx2 = sorted([xs.index(x1) * 2, xs.index(x2) * 2])
    cy1, cy2 = sorted([ys.index(y1) * 2, ys.index(y2) * 2])
    for cx in range(cx1, cx2 + 1):
        for cy in range(cy1, cy2 + 1):
            grid[cx][cy] = 1

outside = {(-1, -1)}
queue = deque(outside)

while len(queue) > 0:
    tx, ty = queue.popleft()
    for nx, ny in [(tx - 1, ty), (tx + 1, ty), (tx, ty - 1), (tx, ty + 1)]:
        if nx < -1 or ny < -1 or nx > len(grid) or ny > len(grid[0]):
            continue
        if (0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and
                grid[nx][ny] == 1):
            continue
        if (nx, ny) in outside:
            continue
        outside.add((nx, ny))
        queue.append((nx, ny))

for x in range(len(grid)):
    for y in range(len(grid[0])):
        if (x, y) not in outside:
            grid[x][y] = 1

psa = [[0] * len(row) for row in grid]
for x in range(len(psa)):
    for y in range(len(psa[0])):
        left = psa[x - 1][y] if x > 0 else 0
        top = psa[x][y - 1] if y > 0 else 0
        topleft = psa[x - 1][y - 1] if x > 0 < y else 0
        psa[x][y] = left + top - topleft + grid[x][y]


def valid(x1, y1, x2, y2):
    cx1, cx2 = sorted([xs.index(x1) * 2, xs.index(x2) * 2])
    cy1, cy2 = sorted([ys.index(y1) * 2, ys.index(y2) * 2])
    left = psa[cx1 - 1][cy2] if cx1 > 0 else 0
    top = psa[cx2][cy1 - 1] if cy1 > 0 else 0
    topleft = psa[cx1 - 1][cy1 - 1] if cx1 > 0 < cy1 else 0
    count = psa[cx2][cy2] - left - top + topleft
    return count == (cx2 - cx1 + 1) * (cy2 - cy1 + 1)


max_area = max(
    (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
    for i, (x1, y1) in enumerate(points)
    for x2, y2 in points[:i]
    if valid(x1, y1, x2, y2)
)

print(max_area)
