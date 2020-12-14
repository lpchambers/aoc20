#!/usr/bin/python3
with open('input') as f:
    lines = [line.strip() for line in f.readlines()]


mask = 0

mem = {}

def calc_mask(inp, mask):
    outp = list(bin(inp)[2:].rjust(36, '0'))
    print(outp)
    for ix, c in enumerate(mask):
        print(ix, c)
        if c == 'X':
            continue
        outp[ix] = c
    return int("".join(outp), 2)
            

for line in lines:
    if line.startswith('mask'):
        mask = line.split()[-1]
    else:
        addr = line.split('[')[1].split(']')[0]
        inp = int(line.split(' = ')[1])
        mem[addr] = calc_mask(inp, mask)

print(sum(mem.values()))
