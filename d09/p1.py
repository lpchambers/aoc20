#!/usr/bin/python3
with open('input') as f:
    lines = [int(x.strip()) for x in f.readlines()]


preamble = lines[:25]

def can_sum_to(l, num):
    for ix, x in enumerate(l):
        for iy, y in enumerate(l):
            if ix == iy:
                continue
            if x + y == num:
                return True
    return False

for val in lines[25:]:
    if not can_sum_to(preamble, val):
        print(val)
        break
    else:
        preamble.pop(0)
        preamble.append(val)

target = val

for x in range(len(lines)):
    for y in range(x+1, len(lines)):
        if sum(lines[x:y]) == target:
            mx = max(lines[x:y])
            mn = min(lines[x:y])
            print(mn + mx)
            import sys
            sys.exit()
