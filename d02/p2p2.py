#!/bin/python3
with open('input') as f:
    l = f.read()

entries = l.splitlines()

n = 0
for e in entries:
    nums, lets, pw = e.split()
    low, high = nums.split('-')
    low = int(low)
    high = int(high)

    let = lets[0]
    print(low, high, let, pw)
    low_in = pw[low-1] == let
    high_in = pw[high-1] == let
    if low_in ^ high_in:
        n += 1
print(n)
