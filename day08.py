# Day 8: Playground

import load_data as ld
import os
import numpy as np
import heapq
import math

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

three_largest = heapq.nlargest(3, (len(lst) for lst in circuits))
print(three_largest[0] * three_largest[1] * three_largest[2])

# Part 2
# Pick up where we left off
# print(len(circuits))
# print(len(flat))
# next_closest_n = num_smallest + 1
# while len(circuits) > 1:
#     # next closest distance
#     idx_next = np.argpartition(flat, next_closest_n - 1)[next_closest_n - 1]
#     r, c = np.unravel_index(idx_next, distances.shape)
#     # connect circuits
#     new_circuit = True
#     i = 0
#     while i < len(circuits):
#         if r in circuits[i] and c in circuits[i]:
#             # r and c both already in circuit
#             new_circuit = False
#             i = len(circuits)
#         elif r in circuits[i]:
#             # See if c is in a different circuit
#             # circuits 0-i have already been considered
#             j = i + 1
#             c_in_circuits = False
#             while j < len(circuits):
#                 if c in circuits[j]:
#                     c_in_circuits = True
#                     jc = j
#                     j = len(circuits)
#                 j += 1
#             # If not, just append c
#             if c_in_circuits:
#                 circuits[i].extend(circuits[jc])
#                 circuits.pop(jc)
#             else:
#                 circuits[i].append(c)
#             new_circuit = False
#             i = len(circuits)
#         elif c in circuits[i]:
#             # See if r is in a different circuit
#             j = i + 1
#             r_in_circuits = False
#             while j < len(circuits):
#                 if r in circuits[j]:
#                     r_in_circuits = True
#                     jr = j
#                     j = len(circuits)
#                 j += 1
#             # If not, just append r
#             if r_in_circuits:
#                 circuits[i].extend(circuits[jr])
#                 circuits.pop(jr)
#             else:
#                 circuits[i].append(r)
#             new_circuit = False
#             i = len(circuits)
#         else:
#             i += 1
#     if new_circuit:
#         circuits.append([r, c])
#     next_closest_n += 1
#     if len(circuits) == 1:
#         print(pos[r][0] * pos[c][0])

# 8362885995 too low

# Following HyperNeutrino's solution

data = ld.load_data(f"example{day}.txt")
data = ld.load_data(f"input{day}.txt")

boxes = [list(map(int, line.split(','))) for line in data]
edges = [(i, j) for i in range(len(boxes)) for j in range(i + 1, len(boxes))]
edges.sort(
    key=lambda x: math.hypot(
        *[a - b for a, b in zip(boxes[x[0]], boxes[x[1]])]
    )
)

parent = list(range(len(boxes)))


def root(x):
    if parent[x] == x:  # it's already the root
        return x
    parent[x] = root(parent[x])  # path compression
    return parent[x]


def merge(a, b):
    parent[root(a)] = root(b)


# Part 1
# for a, b in edges[:1000]:
#     merge(a, b)

# sizes = [0] * len(boxes)

# for box in range(len(boxes)):
#     sizes[root(box)] += 1

# sizes.sort(reverse=True)

# print(sizes[0] * sizes[1] * sizes[2])

# Part 2
circuits = len(boxes)

for a, b in edges:
    if root(a) == root(b):
        continue
    merge(a, b)
    circuits -= 1
    if circuits == 1:
        print(boxes[a][0] * boxes[b][0])
        break
