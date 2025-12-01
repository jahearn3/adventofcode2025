# Day 1: Secret Entrance

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f"example{day}.txt")
data = ld.load_data(f"input{day}.txt")

dial = 50
n_zeros = 0

for line in data:
    direction, magnitude = line[0], int(line[1:])
    if direction == 'R':
        dial += magnitude
    elif direction == 'L':
        dial -= magnitude
    if dial % 100 == 0:
        n_zeros += 1
print(n_zeros)

dial = 50
zero_crossings = 0

for line in data:
    direction, magnitude = line[0], int(line[1:])
    dial_prev = dial
    if direction == 'R':
        dial += magnitude
        step = 1
    elif direction == 'L':
        dial -= magnitude
        step = -1
    for i in range(dial_prev, dial, step):
        if i % 100 == 0:
            zero_crossings += 1

print(zero_crossings)