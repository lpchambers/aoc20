#!/usr/bin/python3
inp = [14,8,16,0,1,17]
target = 2020

#inp = [0, 3, 6]
#target = 10

last_spoken = {val: idx + 1 for idx, val in enumerate(inp)}

turn = len(inp) + 1
last = inp[-1]
del last_spoken[last]

while turn <= target:
    if last not in last_spoken:
        say = 0
    else:
        say = turn - last_spoken[last] - 1

    last_spoken[last] = turn - 1
    turn += 1
    last = say

print(last)
