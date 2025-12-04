# Day 4: Printing Department

import load_data as ld
import os
import time

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f"example{day}.txt")
data = ld.load_data(f"input{day}.txt")


start_time = time.perf_counter()
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

end_time = time.perf_counter()
print(accessible_rolls, end_time - start_time)

# Part 2: Iterative removal
start_time = time.perf_counter()


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
end_time = time.perf_counter()
print(initial_rolls - final_rolls, end_time - start_time)
start_time = time.perf_counter()


def count_accessible_rolls(data):
    R, C = len(data), len(data[0])
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                 (0, 1), (1, -1), (1, 0), (1, 1)]

    accessible_count = 0

    for r in range(R):
        for c in range(C):
            if data[r][c] != '@':
                continue
            adj = 0
            for dr, dc in neighbors:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and data[nr][nc] == '@':
                    adj += 1
            if adj < 4:
                accessible_count += 1

    return accessible_count


accessible_rolls = count_accessible_rolls(data)
end_time = time.perf_counter()
print(accessible_rolls, end_time - start_time)


def count_accessible(r, c, grid, R, C, neighbors):
    if grid[r][c] != '@':
        return False
    adj = 0
    for dr, dc in neighbors:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == '@':
            adj += 1
    return adj < 4


def total_removed_rolls(data):
    R, C = len(data), len(data[0])
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                 (0, 1), (1, -1), (1, 0), (1, 1)]

    removed = 0

    while True:
        to_remove = []
        # find all currently accessible rolls
        for r in range(R):
            for c in range(C):
                if count_accessible(r, c, data, R, C, neighbors):
                    to_remove.append((r, c))

        if not to_remove:
            break  # no more removable rolls

        removed += len(to_remove)

        # remove them simultaneously
        new_rows = [list(row) for row in data]
        for r, c in to_remove:
            new_rows[r][c] = '.'
        data = ["".join(row) for row in new_rows]

    return removed


start_time = time.perf_counter()
removed_rolls = total_removed_rolls(data)
end_time = time.perf_counter()
print(removed_rolls, end_time - start_time)
