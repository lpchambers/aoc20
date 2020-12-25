#!/usr/bin/python3
card_pub = 9232416
door_pub = 14144084
d = 20201227
subject = 7
value = 1
loop = 0
while value != card_pub:
    value = (value * subject) % d
    loop += 1
subject = door_pub
value = 1
for _ in range(loop):
    value = (value * subject) % d
print(value)
