#!/bin/python3
with open('input') as f:
    l = f.read()

entries = [int(x) for x in l.splitlines()]

print(entries)

for a in entries:
    for b in entries:
        for c in entries:
            if a + b + c == 2020:
                print(a * b * c)
                break

