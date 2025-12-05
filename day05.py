# Day 5: Cafeteria

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f"example{day}.txt")
data = ld.load_data(f"input{day}.txt")

fresh_ranges = []
available_ids = []
second_half = False
for line in data:
    if len(line) == 0:
        second_half = True
    elif second_half:
        available_ids.append(int(line))
    else:
        fresh_ranges.append(line)

fresh_count = 0

for id in available_ids:
    spoiled = True
    for r in fresh_ranges:
        min_val, max_val = [int(x) for x in r.split('-')]
        if min_val <= id <= max_val:
            spoiled = False
    if not spoiled:
        fresh_count += 1

print(fresh_count)

# Part 2
intervals = []
for r in fresh_ranges:
    start, end = map(int, r.split('-'))
    intervals.append((start, end))
# Sort the intervals by start values in ascending order
intervals.sort(key=lambda x: x[0])
merged = []
current_start, current_end = intervals[0]
for start, end in intervals[1:]:
    # Check if intervals overlap or are contiguous
    if start <= current_end + 1:
        # Merge intervals
        current_end = max(current_end, end)
    else:
        # Current interval is complete
        merged.append((current_start, current_end))
        # Move on to the next interval
        current_start, current_end = start, end
merged.append((current_start, current_end))
print(sum(end - start + 1 for start, end in merged))
