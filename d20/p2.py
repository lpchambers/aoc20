#!/usr/bin/python3
import math
import regex as re

#with open('example') as f:
with open('input') as f:
    lines = [x.strip() for x in f.readlines()]

tile = None

all_tiles = {}

for line in lines:
    if not line:
        continue
    if line.startswith('Tile'):
        tile = int(line.split()[1].strip(':'))
        all_tiles[tile] = []
        continue
    
    all_tiles[tile].append(line)

N = int(math.sqrt(len(all_tiles)))

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


matches = {t: set() for t in tile_edges.keys()}

for t1, e1 in tile_edges.items():
    for t2, e2 in tile_edges.items():
        if t1 == t2:
            continue
        for edge in e1:
            if edge in e2:
                matches[t1].add(t2)

num_matches = {k: len(v) for k, v in matches.items()}

match2 = [tile for tile, num in num_matches.items() if num == 2]
match3 = [tile for tile, num in num_matches.items() if num == 3]
match4 = [tile for tile, num in num_matches.items() if num == 4]

# print(len(match2))  # Always 4
# print(len(match3))  # 4 * (N-2)
# print(len(match4))  # (N-2) ** 2

if len(match2) != 4:
    print("2 match fail")
if len(match3) != 4 * (N - 2):
    print("3 match fail")
if len(match4) != (N - 2) ** 2:
    print("4 match fail")


if len(match2) == 4:
    res = math.prod(match2)
    print(f"Answer P1: {res}")


def flip_LR(lines):
    return [l[::-1] for l in lines]

def flip_UD(lines):
    return lines[::-1]

def rot90(lines):
    retlines = []
    for rix in range(len(lines)):
        retlines.append("".join([l[rix] for l in lines[::-1]]))
    return retlines

def rotation(lines, rot):
    # Rotates / flips the given "rot" to be EAST
    # rot 0 = top          | 90 clock
    # rot 1 = right        | (no change)
    # rot 2 = bot          | flip UD, 90 clock
    # rot 3 = left         | flip LR
    # rot 4 = top reversed | flip LR, 90 clock
    # rot 5 = right rev    | flip UD
    # rot 6 = bot rev      | flip LR, flip UD, 90 clock
    # rot 7 = left rev     | flip UD, flip LR
    if rot in [4,6]:
        lines = flip_LR(lines)
        rot -= 4
    elif rot in [5,7]:
        lines = flip_UD(lines)
        rot -= 4

    if rot == 0:
        lines = rot90(lines)
    elif rot == 1:
        pass
    elif rot == 2:
        lines = flip_UD(lines)
        lines = rot90(lines)
    elif rot == 3:
        lines = flip_LR(lines)
    return lines



tile_location = {}
placed_tiles = set()

# { (rix, cix): {'E': "##..##.", 'S': "####..."}}
edge_locations = {}

# (rix, cix): ["##..", "..##']
tiles_rotated = {}


# Rotation doesn't matter
for rix in range(N):
    for cix in range(N):
        if rix == 0 and cix == 0:
            # First one doesn't matter
            tile = match2[0]
            tile_location[(rix, cix)] = tile
            placed_tiles.add(tile)
            continue

        if rix == 0 and cix != (N-1):
            behind = tile_location[(rix, cix-1)]
            above = behind
            n_to_match = 3
        elif rix == 0 and cix == (N-1):
            behind = tile_location[(rix, cix-1)]
            above = behind
            n_to_match = 2
        elif cix == 0 and rix != (N-1):
            above = tile_location[(rix-1, cix)]
            behind = above
            n_to_match = 3
        elif cix == 0 and rix == (N-1):
            above = tile_location[(rix-1, cix)]
            behind = above
            n_to_match = 2
        else:
            above = tile_location[(rix-1, cix)]
            behind = tile_location[(rix, cix-1)]
            if rix == (N-1) and cix == (N-1):
                n_to_match = 2
            elif rix == (N-1) or cix == (N-1):
                n_to_match = 3
            else:
                n_to_match = 4

        possibles = matches[above].intersection(matches[behind])
        for possible in possibles:
            if num_matches[possible] == n_to_match and possible not in placed_tiles:
                tile_location[(rix, cix)] = possible
                placed_tiles.add(possible)
                break

        # Special case row 0, col 1 because we don't have first
        if rix == 0 and cix == 1:
            t0 = tile_location[(0, 0)]
            t1 = tile_location[(0, 1)]
            edges1 = tile_edges[t0]
            edges2 = tile_edges[t1]
            lines1 = all_tiles[t0]
            lines2 = all_tiles[t1]
            for e1x, e1 in enumerate(edges1):
                for e2x, e2 in enumerate(edges2):
                    if e1 == e2:
                        l1 = rotation(lines1, e1x)
                        l2 = rotation(lines2, e2x)
                        l2 = flip_LR(l2)
                        tiles_rotated[(0,0)] = l1
                        tiles_rotated[(0,1)] = l2
                        break
                if (0,0) in tiles_rotated:
                    break
        elif rix != 0:
            # match above
            to_match = tiles_rotated[(rix-1, cix)][-1]
            tile = tile_location[(rix, cix)]
            for ex, e in enumerate(tile_edges[tile]):
                if e == to_match:
                    lines = rotation(all_tiles[tile], ex)
                    lines = rot90(rot90(rot90(lines)))
                    tiles_rotated[(rix, cix)] = lines
                    break
        else:
            # match before
            before_tile_rot = tiles_rotated[(rix, cix-1)]
            to_match = "".join([l[-1] for l in before_tile_rot])
            tile = tile_location[(rix, cix)]
            for ex, e in enumerate(tile_edges[tile]):
                if e == to_match:
                    lines = rotation(all_tiles[tile], ex)
                    lines = flip_LR(lines)
                    tiles_rotated[(rix, cix)] = lines
                    break



def put_together(loc_to_lines, N):
    IN = len(loc_to_lines[(0,0)])
    lines = [""] * IN * N
    for rix in range(N):
        for cix in range(N):
            tlines = loc_to_lines[(rix, cix)]
            for rx, tline in enumerate(tlines):
                lines[IN*rix + rx] += tline

    return lines


def strip_border(lines):
    l = lines.copy()
    l = lines[1:-1]
    l = [x[1:-1] for x in l]
    return l


tiles_stripped = {k: strip_border(v) for k, v in tiles_rotated.items()}

mon1 = "^                  #".replace(" ", ".")
mon2 = "#    ##    ##    ###".replace(" ", ".")
mon3 = " #  #  #  #  #  #".replace(" ", ".")

mon1_indexes = set(mon1.index('#', n) - 1 for n in range(len(mon1)))
mon2_indexes = set(mon2.index('#', n) for n in range(len(mon2)))
mon3_indexes = set(mon3.index('#', n) for n in range(len(mon3)))

MON_LEN = (mon1 + mon2 + mon3).count('#')

search_grid = put_together(tiles_stripped, N)

num_mon = 0

rot = 2  # Found

while num_mon == 0:
    num_mon = 0
    print(f"Testing rotation {rot}")
    test_search_grid = rotation(search_grid, rot)
    rot += 1
    for ix, line in enumerate(test_search_grid[:-2]):
        l1 = test_search_grid[ix]
        l2 = test_search_grid[ix+1]
        l3 = test_search_grid[ix+2]
        m2 = re.findall(mon2, l2, overlapped=True)
        m3 = re.findall(mon3, l3, overlapped=True)

        if m2 and m3:
            i2 = set([l2.index(t) for t in m2])
            i3 = set([l3.index(t) for t in m3])
            inter = i2.intersection(i3)
            if inter:
                for match_ix in sorted(list(inter)):
                    if re.match(mon1, l1[match_ix:]):
                        print(ix, match_ix)
                        print(l1[match_ix:match_ix+20])
                        print(l2[match_ix:match_ix+20])
                        print(l3[match_ix:match_ix+20])
                        num_mon += 1
                        # Replace # with 'O'
                        for rx in mon1_indexes:
                            rrx = rx + match_ix
                            l1 = l1[:rrx] + 'O' + l1[rrx+1:]
                        for rx in mon2_indexes:
                            rrx = rx + match_ix
                            l2 = l2[:rrx] + 'O' + l2[rrx+1:]
                        for rx in mon3_indexes:
                            rrx = rx + match_ix
                            l3 = l3[:rrx] + 'O' + l3[rrx+1:]
                        test_search_grid[ix] = l1
                        test_search_grid[ix + 1] = l2
                        test_search_grid[ix + 2] = l3

    print(f"Num monster {num_mon}")


print(len(test_search_grid), len(test_search_grid[0]))
print("\n".join(test_search_grid))
with open("result", 'w') as f:
    f.write("\n".join(test_search_grid))
print(f"Number monsters: {num_mon}")
totat_hash = "".join(test_search_grid).count('#')
print(f"Water roughness: {totat_hash}")

# Not 2213 2648    2324 2297     2427     (2205)
