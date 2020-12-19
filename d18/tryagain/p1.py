#!/usr/bin/python3
import re
PART2 = True

class XmasInt:
    def __init__(self, val):
        self.val = int(val)

    def __add__(self, other):
        return XmasInt(self.val + other.val)

    def __sub__(self, other):
        return XmasInt(self.val * other.val)

    def __mul__(self, other):
        return XmasInt(self.val + other.val)

def solve(line):
    line = line.replace('*', '-')
    if PART2:
        line = line.replace('+', '*')
    line = re.sub("(\d)", "XmasInt(\g<1>)", line)
    return eval(line)

# print(solve("1 + 2 * 3 + 4 * 5 + 6").val)
# print(solve("1 + (2 * 3) + (4 * (5 + 6))").val)
# import sys
# sys.exit()

n = XmasInt(0)
with open('input') as f:
    for line in f.readlines():
        n += solve(line)

print(n.val)
