#!/usr/bin/python3
with open('input') as f:
    lines = [line.strip() for line in f.readlines()]


mask = 0

mem = {}

def _recur_mem(raw):
    if 'X' not in raw:
        return [int("".join(raw), 2)]

    mems = []
    for ix, c in enumerate(raw):
        if c == 'X':
            r0 = raw.copy()
            r0[ix] = '0'
            r1 = raw.copy()
            r1[ix] = '1'
            mems.extend(_recur_mem(r0))
            mems.extend(_recur_mem(r1))
            return mems

        

def calc_masks(inp, mask):
    print(inp)
    outp = list(bin(int(inp))[2:].rjust(36, '0'))
    print(outp)
    for ix, c in enumerate(mask):
        if c == '0':
            continue
        outp[ix] = c

    return _recur_mem(outp)
            

for line in lines:
    if line.startswith('mask'):
        mask = line.split()[-1]
    else:
        addr = line.split('[')[1].split(']')[0]
        inp = int(line.split(' = ')[1])
        for store_addr in calc_masks(addr, mask):
            mem[store_addr] = inp

print(sum(mem.values()))
