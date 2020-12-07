#!/bin/python3
with open('input') as f:
    lines = f.read()

entries = lines.splitlines()

def test(DR, DC):
    r = 0
    c = 0
    hits = 0
    l = len(entries[0])
    for row in entries[::DR]:
        if row[c] == '#':
            hits += 1
        c = (c + DC) % l
    return hits

print(test(1,1) * test(1,3) * test(1,5) * test(1,7) * test(2,1))
