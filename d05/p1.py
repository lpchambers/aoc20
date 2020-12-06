#!/usr/bin/python3
with open('input') as f:
    lines = f.readlines()


ids = []
for l in lines:
    b = l.strip().replace('B', '1').replace('F', '0').replace("R", "1").replace("L", "0")
    idx = int(b, 2)
    ids.append(idx)

print(max(ids))

s = sorted(ids)
n = s[0] - 1
for x in s:
    if n != x - 1:
        print(x-1)
        break
    n = x






























# Golf
ids = [int(l.strip().replace('B', '1').replace('F', '0').replace("R", "1").replace("L", "0"), 2) for l in open('input').readlines()]
sorted_ids = sorted(ids)
for idx, val in enumerate(sorted_ids):
    if (idx != 0) and (sorted_ids[idx-1] != val - 1):
        print(max(ids), val - 1)
