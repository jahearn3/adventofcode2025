# Day 9: Movie Theater

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f"example{day}.txt")
# data = ld.load_data(f"input{day}.txt")

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
