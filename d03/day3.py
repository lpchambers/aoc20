#!/bin/python3
with open('input') as f:
    lines = f.read()

DR = 1
DC = 3

entries = lines.splitlines()

r = 0
c = 0
hits = 0
l = len(entries[0])
for row in entries:
    print(row)
    if row[c] == '#':
        hits += 1
    c = (c + DC) % l

print(hits)
