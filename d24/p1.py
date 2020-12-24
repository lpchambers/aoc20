#!/usr/bin/python3
with open('input') as f:
    lines = [x.strip() for x in f.readlines()]

# lines = """sesenwnenenewseeswwswswwnenewsewsw
# neeenesenwnwwswnenewnwwsewnenwseswesw
# seswneswswsenwwnwse
# nwnwneseeswswnenewneswwnewseswneseene
# swweswneswnenwsewnwneneseenw
# eesenwseswswnenwswnwnwsewwnwsene
# sewnenenenesenwsewnenwwwse
# wenwwweseeeweswwwnwwe
# wsweesenenewnwwnwsenewsenwwsesesenwne
# neeswseenwwswnwswswnw
# nenwswwsewswnenenewsenwsenwnesesenew
# enewnwewneswsewnwswenweswnenwsenwsw
# sweneswneswneneenwnewenewwneswswnese
# swwesenesewenwneswnwwneseswwne
# enesenwswwswneneswsenwnewswseenwsese
# wnwnesenesenenwwnenwsewesewsesesew
# nenewswnwewswnenesenwnesewesw
# eneswnwswnwsenenwnwnwwseeswneewsenese
# neswnwewnwnwseenwseesewsenwsweewe
# wseweeenwnesenwwwswnew""".splitlines()


# Set of coords
black = set()


for line in lines:
    i = 0
    x = 0
    y = 0
    while i < len(line):
        c0 = line[i]
        if c0 == 'e':
            x += 1
        elif c0 == 'w':
            x -= 1
        elif c0 == 'n':
            i += 1
            c1 = line[i]
            y += 1
            if c1 == 'w':
                x -= 1
        elif c0 == 's':
            i += 1
            c1 = line[i]
            y -= 1
            if c1 == 'e':
                x += 1
        i += 1

    if (x,y) in black:
        black.remove((x,y))
    else:
        black.add((x,y))

print(len(black))


def get_around(p):
    d = [(0,1), (1,0), (1,-1), (0,-1), (-1,0), (-1,1)]
    return [(p[0] + dx, p[1] + dy) for dx, dy in d]

def num_around(tile, blacks):
    n = 0
    for p in get_around(tile):
        if p in blacks:
            n+=1
    return n

white = set()

for _ in range(100):
    new_black = set()
    new_white = set()

    # Pad out whites
    for b in black:
        for p in get_around(b):
            if p not in white:
                white.add(p)

    for b in black:
        num = num_around(b, black)
        if num == 0 or num > 2:
            new_white.add(b)
        else:
            new_black.add(b)

    for w in white:
        num = num_around(w, black)
        if num == 2:
            new_black.add(w)
        else:
            new_white.add(w)


    black = new_black
    white = new_white

print(len(black))
