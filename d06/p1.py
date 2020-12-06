#!/usr/bin/python3
with open('input') as f:
    lines = f.readlines()

lines = [l.strip() for l in lines]
lines.append("")

s1 = set()
n1 = 0

s2 = None
n2 = 0


for l in lines:
    if l:
        for char in l:
            s1.add(char)
        new2 = set(x for x in l)
        if s2 is not None:
            s2 = s2.intersection(new2)
        else:
            s2 = new2
        print(s2)
    else:
        n1 += len(s1)
        s1 = set()

        print(len(s2))
        n2 += len(s2)
        s2 = None

print(n1)
print(n2)
