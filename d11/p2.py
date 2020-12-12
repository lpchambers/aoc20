#!/usr/bin/python3
with open('input') as f:
    lines = [x.strip() for x in f.readlines()]

# lines = """L.LL.LL.LL
# LLLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLLL
# L.LLLLLL.L
# L.LLLLL.LL""".splitlines()



empty = []
occ = []
for rix, row in enumerate(lines):
    for cix, val in enumerate(row):
        if val == "L":
            empty.append((rix, cix))


around = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (1, 1),
    (1, -1),
    (-1, -1),
    (-1, 1),
]

NR = len(lines)
NC = len(lines[0])

check_maps = {}
for pos in empty:
    check_maps[pos] = []
    for d in around:
        r = pos[0]
        c = pos[1]
        while True:
            r = r + d[0]
            c = c + d[1]
            if r<0 or r>NR or c<0 or c>NC or (r,c) in empty:
                check_maps[pos].append((r,c))
                break


n = 0
while len(empty) != n:
    n = len(empty)
    new_empty = []
    new_occ = []
    for pos in empty:
        check_pos = [1 for check in check_maps[pos] if check in occ]
        if len(check_pos) == 0:
            new_occ.append(pos)
        else:
            new_empty.append(pos)

    for pos in occ:
        check_pos = [1 for check in check_maps[pos] if check in occ]
        if len(check_pos) >= 5:
            new_empty.append(pos)
        else:
            new_occ.append(pos)

    empty = new_empty
    occ = new_occ
    print(len(occ), len(empty), len(occ)+len(empty))
print(len(occ))
