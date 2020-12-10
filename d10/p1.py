#!/usr/bin/python3
with open('input') as f:
    lines = [int(x.strip()) for x in f.readlines()]

x = sorted(lines)
x.insert(0, 0)
x.append(x[-1] + 3)

delta = [x[i] - x[i-1] for i in range(1,len(x))]
print(delta.count(1) * delta.count(3))

n = 0
runs = []
for y in delta:
    if y == 3:
        runs.append(n-1)
        n = 0
    else:
        n += 1

paths = [y*(y+1)/2 + 1 for y in runs]

s = 1
for y in paths:
    s *= y
print(int(s))

import sys
sys.exit()

import networkx

G = networkx.DiGraph()
for idx, val in enumerate(x):
    G.add_node(val)
    for after in x[idx+1:idx+4]:
        if after - val <= 3:
            G.add_edge(val, after)


n = 1
imin = 0
imax = 0
for idx, val in enumerate(x):
    if idx == len(delta):
        break
    if delta[idx] == 3:
        imax = idx + 1

        print(x[imin:imax+1], x[imin], x[imax])
        all_paths = list(networkx.all_simple_paths(G, x[imin], x[imax]))
        l = len(all_paths)
        print("Number of Paths", l)
        n *= l
        imin = imax
print(n)
