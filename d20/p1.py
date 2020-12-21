#!/usr/bin/python3
import math

#with open('example') as f:
with open('input') as f:
    lines = [x.strip() for x in f.readlines()]

print(lines)
tile = None

all_tiles = {}

for line in lines:
    if not line:
        continue
    if line.startswith('Tile'):
        tile = int(line.split()[1].strip(':'))
        print(tile)
        all_tiles[tile] = []
        continue
    
    all_tiles[tile].append(line)

print(all_tiles)


N = int(math.sqrt(len(all_tiles)))
print(N)

tile_edges = {}
for tile, lines in all_tiles.items():
    edges = [
        lines[0],
        "".join(l[-1] for l in lines),
        lines[-1],
        "".join(l[0] for l in lines),
    ]
    edges.extend([edge[::-1] for edge in edges])
    tile_edges[tile] = edges

print(all_tiles[2311])
print(tile_edges[2311])

matches = {t: set() for t in tile_edges.keys()}

for t1, e1 in tile_edges.items():
    for t2, e2 in tile_edges.items():
        if t1 == t2:
            continue
        for edge in e1:
            if edge in e2:
                matches[t1].add(t2)

print(matches)
num_matches = {k: len(v) for k, v in matches.items()}
print(num_matches)

match2 = [tile for tile, num in num_matches.items() if num == 2]
if len(match2) == 4:
    res = math.prod(match2)
    print(f"Answer P1: {res}")
