# Day 2: Gift Shop

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f"example{day}.txt")
data = ld.load_data(f"input{day}.txt")

ans = 0
invalid_ids = []
id_ranges = data[0].split(',')
for idr in id_ranges:
    first_id, last_id = idr.split('-')
    for i in range(int(first_id), int(last_id) + 1):
        id = str(i)
        first_half, second_half = id[:len(id)//2], id[len(id)//2:]
        if first_half == second_half:
            ans += i
        for j in range(2, len(id) + 1):
            if len(id) % j == 0:
                length = len(id) // j
                pieces = [id[k * length:(k + 1) * length] for k in range(j)]
                if all(piece == pieces[0] for piece in pieces):
                    invalid_ids.append(i)

print(ans)
print(sum(set(invalid_ids)))
