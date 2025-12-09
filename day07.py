# Day 7: Laboratories

import load_data as ld
import os
from functools import cache

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f"example{day}.txt")
data = ld.load_data(f"input{day}.txt")

n_splits = 0
beams = []  # indices of current beam locations
for j, char in enumerate(data[0]):
    if char == 'S':
        beams.append(j)
for line in data[1:]:
    new_beams = []
    for beam in beams:
        if line[beam] == '^':
            new_beams.append(beam-1)
            new_beams.append(beam+1)
            n_splits += 1
        else:
            new_beams.append(beam)
    beams = set(new_beams)

print(n_splits)

# Part 2


@cache  # to avoid duplicate computations
def solve(r, c):
    if r >= len(data):
        return 1  # timeline reaches bottom of grid
    if data[r][c] == '.' or data[r][c] == 'S':
        return solve(r + 1, c)  # pass the beam downward
    elif data[r][c] == '^':
        return solve(r, c - 1) + solve(r, c + 1)  # solve left and right


print(solve(0, data[0].find('S')))
