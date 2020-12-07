#!/bin/python3
with open('input') as f:
    l = f.read()

entries = l.splitlines()

n = 0
for e in entries:
    nums, lets, pw = e.split()
    low, high = nums.split('-')
    low = int(low)
    high = int(high)

    let = lets[0]
    print(low, high, let, pw)
    num_in = pw.count(let)
    if num_in >= low and num_in <= high:
        n+=1
print(n)
