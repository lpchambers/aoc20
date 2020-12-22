#!/usr/bin/python3
with open('input') as f:
    lines = [x.strip() for x in f.readlines()]

p1 = []
p2 = []

DOP2 = False
for line in lines:
    if line.startswith('Player'):
        continue
    if not line:
        DOP2 = True
        continue

    if DOP2:
        p2.append(int(line))
    else:
        p1.append(int(line))

realp1 = p1.copy()
realp2 = p2.copy()

# Part 1
while p1 and p2:
    c1 = p1.pop(0)
    c2 = p2.pop(0)
    if c1 > c2:
        p1.append(c1)
        p1.append(c2)
    else:
        p2.append(c2)
        p2.append(c1)


winner = p1 or p2

def get_points(winner):
    points = [x for x in range(len(winner), 0, -1)]

    tot = [x * y for x, y in zip(winner, points)]
    return sum(tot)

print(get_points(winner))

# part 2
p1 = realp1
p2 = realp2

def recur_combat(p1, p2):
    # Return True for P1 win
    # Return False for P2 win

    states = set()

    while p1 and p2:
        h1 = tuple(p1)
        h2 = tuple(p2)
        s = (h1, h2)
        if s in states:
            return True, p1

        states.add(s)

        c1 = p1.pop(0)
        c2 = p2.pop(0)
        if len(p1) >= c1 and len(p2) >= c2:
            # Subgame
            subp1 = p1.copy()[:c1]
            subp2 = p2.copy()[:c2]
            if recur_combat(subp1, subp2)[0]:
                # P1 win
                p1.append(c1)
                p1.append(c2)
            else:
                p2.append(c2)
                p2.append(c1)
        else:
            # same rules
            if c1 > c2:
                p1.append(c1)
                p1.append(c2)
            else:
                p2.append(c2)
                p2.append(c1)
    if p1:
        return True, p1
    else:
        return False, p2

win, deck = recur_combat(p1, p2)
print(win)
print(deck)
print(get_points(deck))
