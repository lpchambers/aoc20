#!/usr/bin/python3
with open('input') as f:
    lines = [x.strip() for x in f.readlines()]


# lines = """.#.
# ..#
# ###""".splitlines()

print(lines)

active = set()
inactive = set()
for rix, row in enumerate(lines):
    for cix, col in enumerate(row):
        if col == "#":
            active.add((rix, cix, 0))
        else:
            inactive.add((rix, cix, 0))

CYCLES = 6

ones = [-1, 0, 1]
around = [(x,y,z) for x in ones for y in ones for z in ones]
around.remove((0,0,0))


r0 = 0
r1 = len(lines[0]) - 1
c0 = 0
c1 = len(lines) - 1
z0 = 0
z1 = 0
print(r0, r1, c0, c1, z0 ,z1)


def num_around(pos, active):
    n = 0
    for d in around:
        if (pos[0] + d[0], pos[1] + d[1], pos[2] + d[2]) in active:
            n += 1
    return n

for _ in range(CYCLES):
    # ADD INACTIVE AROUND
    r0 -= 1
    r1 += 1
    c0 -= 1
    c1 += 1
    z0 -= 1
    z1 += 1

    for r in range(r0, r1+1):
        for c in range(c0, c1+1):
            for z in range(z0, z1+1):
                p = (r, c, z)
                if p not in active and p not in inactive:
                    inactive.add(p)

    new_active = set()
    new_inactive = set()
    for pos in active:
        if num_around(pos, active) in [2,3]:
            new_active.add(pos)
        else:
            new_inactive.add(pos)
    for pos in inactive:
        if num_around(pos, active) == 3:
            new_active.add(pos)
        else:
            new_inactive.add(pos)

    active = new_active
    inactive = new_inactive


print(len(active))
