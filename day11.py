# Day 11: Reactor

import load_data as ld
import os

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
