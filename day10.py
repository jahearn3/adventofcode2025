# Day 10: Factory

import load_data as ld
import os
import itertools
import z3

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f"example{day}.txt")
data = ld.load_data(f"input{day}.txt")

total = 0

for line in data:
    schematics = line.split(' ')
    indicators = schematics[0].strip('[]')
    buttons = [x.strip('()') for x in schematics[1:-1]]
    end_state = {idx for idx, light in enumerate(indicators) if light == "#"}
    buttons = [set(map(int, button.split(","))) for button in buttons]
    for count in range(1, len(buttons) + 1):
        for attempt in itertools.combinations(buttons, r=count):
            lights = set()
            for button in attempt:
                lights ^= button  # toggling by symmetric difference
            if lights == end_state:
                total += count
                break  # a match was found
        else:  # if a match was not found
            continue  # go to next iteration of count
        break  # if a match was found

print(total)

# Part 2
# Integer Programming
total = 0

for line in data:
    schematics = line.split(' ')
    buttons = [x.strip('()') for x in schematics[1:-1]]
    joltages = schematics[-1].strip('{}')
    buttons = [set(map(int, button.split(','))) for button in buttons]
    joltages = list(map(int, joltages.split(',')))
    o = z3.Optimize()
    vars = z3.Ints(f'n{i}' for i in range(len(buttons)))
    for var in vars:
        o.add(var >= 0)
    for i, joltage in enumerate(joltages):
        equation = 0
        for b, button in enumerate(buttons):
            if i in button:
                equation += vars[b]
        o.add(equation == joltage)
    o.minimize(sum(vars))
    o.check()
    total += o.model().eval(sum(vars)).as_long()

print(total)
