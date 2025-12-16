# Day 12: Christmas Tree Farm

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f"example{day}.txt")
# data = ld.load_data(f"input{day}.txt")

shapes = {}
regions = []
x = False

for line in data:
    if 'x' in line:
        x = True
    if x:
        dim, presents = line.split(': ')
        width, length = dim.split('x')
        presents = list(map(int, presents.split(' ')))
        regions.append((int(width), int(length), presents))
    elif ':' in line:
        k = int(line.strip(':'))
        shapes[k] = []
    elif len(line) > 0:
        shapes[k].append(line)


print(shapes)
print(regions)
ans = 0

for r in regions:
    width, length, presents = r
    presents_to_fit = []
    for p in range(len(presents)):
        for i in range(p):
            presents_to_fit.append(shapes[p])
    print('Region', r)
    print('Shapes to fit:')
    print(presents_to_fit)

print(ans)
