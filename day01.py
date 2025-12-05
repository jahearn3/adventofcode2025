# Day 1: Secret Entrance

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f"example{day}.txt")
data = ld.load_data(f"input{day}.txt")

dial = 50
n_zeros = 0  # For part 1
zero_crossings = 0  # For part 2

for line in data:
    direction, magnitude = line[0], int(line[1:])
    dial_prev = dial
    if direction == 'R':
        dial += magnitude
        step = 1
    elif direction == 'L':
        dial -= magnitude
        step = -1
    if dial % 100 == 0:  # Dial points at zero
        n_zeros += 1
    for i in range(dial_prev, dial, step):
        if i % 100 == 0:  # Dial crosses zero
            zero_crossings += 1

print(n_zeros)
print(zero_crossings)
