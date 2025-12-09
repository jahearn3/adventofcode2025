# Day 6: Trash Compactor

import load_data as ld
import os
from math import prod

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f"example{day}.txt")
data = ld.load_data(f"input{day}.txt")

numbers = []
for i, line in enumerate(data):
    if i == len(data) - 1:
        operations = line.split()
    else:
        numbers.append([int(x) for x in line.split()])
transposed = list(map(list, zip(*numbers)))
totals = []
for i in range(len(transposed)):
    if operations[i] == '+':
        totals.append(sum(transposed[i]))
    elif operations[i] == '*':
        totals.append(prod(transposed[i]))

print(sum(totals))

# Part 2
strings = [''] * len(data[0])
for i in range(len(strings)):
    for j in range(len(data) - 1):
        strings[i] += data[j][i]

numbers = []
n = []
for i, string in enumerate(strings):
    if string.strip() == '':
        numbers.append(n)
        n = []
    else:
        n.append(int(string.strip()))
numbers.append(n)
totals = []
for i in range(len(operations)):
    if operations[i] == '+':
        totals.append(sum(numbers[i]))
    elif operations[i] == '*':
        totals.append(prod(numbers[i]))

print(sum(totals))
