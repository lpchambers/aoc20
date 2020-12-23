#!/usr/bin/python3
inp = "469217538"
#inp = "389125467"

inp = [int(x) for x in inp]
MAX = len(inp)
print(MAX)
cur = inp[0]
cur_ix = 0

for _ in range(100):
    if cur_ix < MAX-4:
        pick = inp[cur_ix+1:cur_ix+4]
        inp = inp[:cur_ix+1] + inp[cur_ix+4:]
    elif cur_ix < MAX-1:
        pick = inp[cur_ix+1:] + inp[:(cur_ix+4)%MAX]
        inp = inp[(cur_ix+4)%MAX:cur_ix+1]
    else:
        pick = inp[:3]
        inp = inp[3:]
    target = cur - 1 % MAX
    if target == 0:
        target = MAX
    while target not in inp:
        target = (target - 1) % MAX
        if target == 0:
            target = MAX
        print('t', target)

    print(cur, target, pick)
    tix = inp.index(target)
    inp = inp[:tix+1] + pick + inp[tix+1:]
    
    # cur_ix moved
    cur_ix = (inp.index(cur) + 1) % MAX
    cur = inp[cur_ix]

    print(inp)

one_ix = inp.index(1)
res = inp[one_ix + 1:] + inp[:one_ix]
print(res)
print("".join([str(x) for x in res]))
