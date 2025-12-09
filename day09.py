# Day 9: Movie Theater

import load_data as ld
import os

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
