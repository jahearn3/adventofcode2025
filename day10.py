# Day 10: Factory

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f"example{day}.txt")
# data = ld.load_data(f"input{day}.txt")

ans = 0
indicator_light_diag = []
button_wiring_schem = []
joltage_reqs = []

for line in data:
    schematics = line.split(' ')
    indicator_light_diag.append(schematics[0].strip('[]'))
    button_wiring_schem.append([x.strip('()') for x in schematics[1:-1]])
    joltage_reqs.append(schematics[-1].strip('{}'))

n_machines = len(indicator_light_diag)


def bfs(indicator_light_diagram, button_wiring_schematic):
    # initialize indicator lights to all off
    indicator_lights = [False] * len(indicator_light_diagram)
    # intialize sequence
    sequence = []
    # set desired final state of indicator lights
    end_state = [True if x == '#' else False for x in indicator_light_diagram]

    while indicator_lights != end_state:
        # toggle the state of indicator lights
        # by pushing any of the listed buttons

        # see if any of them is one push away from end state
        for button in button_wiring_schem:
            connections = map(int, button.split(','))
            for c in connections:
                if indicator_lights[c]:
                    indicator_lights[c] = False
                else:
                    indicator_lights[c] = True
            if indicator_lights == end_state:
                sequence.append(button)

    return len(sequence)


for i in range(n_machines):
    print(button_wiring_schem[i])
    # fewest total presses required to correctly configure all indicator
    # lights for all machines
    ans += bfs(indicator_light_diag[i], button_wiring_schem[i])

print(ans)
