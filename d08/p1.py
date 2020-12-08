#!/usr/bin/python3
with open('input') as f:
    lines = f.readlines()

insts = []
for l in lines:
    op, val = l.strip().split()
    insts.append([op, int(val)])

def run(insts):
    acc = 0
    ip = 0
    visited = []
    while ip not in visited:
        visited.append(ip)
        #if ip < 0 or ip >= len(insts):
        #    return (acc, False)
        #    break
        op, val = insts[ip]
        if op == "nop":
            ip += 1
        elif op == "acc":
            ip += 1
            acc += val
        elif op == "jmp":
            ip += val
    else:
        return (acc, True)
    return (acc, False)

print(run(insts))
for idx, _ in enumerate(insts):
    itest = insts.copy()
    if itest[idx][0] == "nop":
        itest[idx][0] = "jmp"
    elif itest[idx][0] == "jmp":
        itest[idx][0] = "nop"
    else:
        continue

    acc, fail = run(itest)
    if not fail:
        print(acc)
        break
