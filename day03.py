# Day 3: Lobby

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f"example{day}.txt")
data = ld.load_data(f"input{day}.txt")

digits = ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']
for limit in [2, 12]:
    ans = 0
    for line in data:
        i = 0
        joltage = ''
        idx_max = len(line) - limit + 1
        idx_min = 0
        while len(joltage) < limit:
            if digits[i] in line[idx_min:idx_max]:
                joltage += digits[i]
                idx_min = line[idx_min:idx_max].find(digits[i]) + 1 + idx_min
                idx_max += 1
                i = -1  # it will be increased to 0 at the end of the loop
            if len(joltage) == limit:
                ans += int(joltage)
            i += 1

    print(ans)
