# Day 4: Printing Department

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f"example{day}.txt")
data = ld.load_data(f"input{day}.txt")

accessible_rolls = 0

for r, line in enumerate(data):
    for c, char in enumerate(line):
        if char == '@':
            adjacent_rolls = 0
            if 0 < r:
                if 0 < c:
                    if data[r-1][c-1] == '@':
                        adjacent_rolls += 1
                if data[r-1][c] == '@':
                    adjacent_rolls += 1
                if c < len(line) - 1:
                    if data[r-1][c+1] == '@':
                        adjacent_rolls += 1
            if 0 < c:
                if data[r][c-1] == '@':
                    adjacent_rolls += 1
            if c < len(line) - 1:
                if data[r][c+1] == '@':
                    adjacent_rolls += 1
            if r < len(data) - 1:
                if 0 < c:
                    if data[r+1][c-1] == '@':
                        adjacent_rolls += 1
                if data[r+1][c] == '@':
                    adjacent_rolls += 1
                if c < len(line) - 1:
                    if data[r+1][c+1] == '@':
                        adjacent_rolls += 1

            if adjacent_rolls < 4:
                accessible_rolls += 1

print(accessible_rolls)

# Part 2: Iterative removal


def remove_accessible_rolls(grid):
    accessible_rolls = 0
    new_grid = grid.copy()
    for r, line in enumerate(grid):
        for c, char in enumerate(line):
            if char == '@':
                adjacent_rolls = 0
                if 0 < r:
                    if 0 < c:
                        if grid[r-1][c-1] == '@':
                            adjacent_rolls += 1
                    if grid[r-1][c] == '@':
                        adjacent_rolls += 1
                    if c < len(line) - 1:
                        if grid[r-1][c+1] == '@':
                            adjacent_rolls += 1
                if 0 < c:
                    if grid[r][c-1] == '@':
                        adjacent_rolls += 1
                if c < len(line) - 1:
                    if grid[r][c+1] == '@':
                        adjacent_rolls += 1
                if r < len(grid) - 1:
                    if 0 < c:
                        if grid[r+1][c-1] == '@':
                            adjacent_rolls += 1
                    if grid[r+1][c] == '@':
                        adjacent_rolls += 1
                    if c < len(line) - 1:
                        if grid[r+1][c+1] == '@':
                            adjacent_rolls += 1

                if adjacent_rolls < 4:
                    accessible_rolls += 1
                    modified = line[:c] + '.' + line[c+1:]
                    new_grid[r] = modified

    return accessible_rolls, new_grid


initial_rolls = 0
for line in data:
    for char in line:
        if char == '@':
            initial_rolls += 1

removed = []
accessible_rolls = None
grid = data
while accessible_rolls != 0:
    accessible_rolls, grid = remove_accessible_rolls(grid)
    removed.append(accessible_rolls)

final_rolls = 0
for line in grid:
    for char in line:
        if char == '@':
            final_rolls += 1
print(initial_rolls - final_rolls)
