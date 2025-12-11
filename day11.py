# Day 11: Reactor

import load_data as ld
import os
from functools import lru_cache
import sys

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f"example{day}.txt")
data = ld.load_data(f"input{day}.txt")

devices = {}
for line in data:
    k, v = line.split(': ')
    devices[k] = []
    for vv in v.split(' '):
        devices[k].append(vv)

start = 'you'
end = 'out'
ans = 0  # number of paths from you to out

# dfs
stack = [start]
while stack:
    node = stack.pop()
    if node == end:
        ans += 1
    else:
        stack.extend(x for x in devices[node])

print(ans)

# Part 2
data = ld.load_data(f"example{day}b.txt")
data = ld.load_data(f"input{day}.txt")

devices = {}
for line in data:
    k, v = line.split(': ')
    devices[k] = []
    for vv in v.split(' '):
        devices[k].append(vv)

sys.setrecursionlimit(10**7)
start = 'svr'
end = 'out'


@lru_cache(maxsize=None)
def count_paths(node, visited_dac, visited_fft):
    # Update flags
    visited_dac = visited_dac or (node == 'dac')
    visited_fft = visited_fft or (node == 'fft')

    if node == end:
        return int(visited_dac and visited_fft)

    total = 0
    for nxt in devices.get(node, []):
        total += count_paths(nxt, visited_dac, visited_fft)
    return total


ans = count_paths(start, False, False)
print(ans)
