# Day 8: Playground

import load_data as ld
import os
import numpy as np
import heapq

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f"example{day}.txt")
data = ld.load_data(f"input{day}.txt")

pos = []
for line in data:
    x, y, z = line.split(',')
    pos.append((int(x), int(y), int(z)))

n = len(pos)
distances = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i <= j:
            distances[i][j] = np.inf
        else:
            dx = (pos[i][0] - pos[j][0])**2
            dy = (pos[i][1] - pos[j][1])**2
            dz = (pos[i][2] - pos[j][2])**2
            distances[i][j] = np.sqrt(dx + dy + dz)

num_smallest = 10  # for the example
num_smallest = 1000  # for the puzzle

flat = distances.flatten()
smallest_indices = np.argpartition(flat, num_smallest - 1)[:num_smallest]
rows, cols = np.unravel_index(smallest_indices, distances.shape)
result = [(int(r), int(c)) for r, c in zip(rows, cols)]

circuits = []

for r, c in result:
    if len(circuits) == 0:
        circuits.append([r, c])
    else:
        new_circuit = True
        i = 0
        while i < len(circuits):
            if r in circuits[i] and c in circuits[i]:
                # r and c both already in circuit
                new_circuit = False
                i = len(circuits)
            elif r in circuits[i]:
                # See if c is in a different circuit
                # circuits 0-i have already been considered
                j = i + 1
                c_in_circuits = False
                while j < len(circuits):
                    if c in circuits[j]:
                        c_in_circuits = True
                        jc = j
                        j = len(circuits)
                    j += 1
                # If not, just append c
                if c_in_circuits:
                    circuits[i].extend(circuits[jc])
                    circuits.pop(jc)
                else:
                    circuits[i].append(c)
                new_circuit = False
                i = len(circuits)
            elif c in circuits[i]:
                # See if r is in a different circuit
                j = i + 1
                r_in_circuits = False
                while j < len(circuits):
                    if r in circuits[j]:
                        r_in_circuits = True
                        jr = j
                        j = len(circuits)
                    j += 1
                # If not, just append r
                if r_in_circuits:
                    circuits[i].extend(circuits[jr])
                    circuits.pop(jr)
                else:
                    circuits[i].append(r)
                new_circuit = False
                i = len(circuits)
            else:
                i += 1
        if new_circuit:
            circuits.append([r, c])

# print(len(circuits))
# print(circuits)

three_largest = heapq.nlargest(3, (len(lst) for lst in circuits))
print(three_largest[0] * three_largest[1] * three_largest[2])
