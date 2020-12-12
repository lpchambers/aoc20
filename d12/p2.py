#!/usr/bin/python3
with open('input') as f:
    dirs = [(line[0], int(line[1:].strip())) for line in f.readlines()]

movement = {
    'N': (1, 0),
    'S': (-1, 0),
    'E': (0, 1),
    'W': (0, -1),
}

pos = (0, 0)
wp = (1, 10)

for action, value in dirs:
    if action == "F":
        pos = (pos[0] + value * wp[0], pos[1] + value * wp[1])
    elif action in movement:
        add = movement[action]
        wp = (wp[0] + value * add[0], wp[1] + value * add[1])
    elif action in 'LR':
        if value == 180:
            wp = (-wp[0], -wp[1])
        elif (value == 90 and action == "L") or (value == 270 and action == "R"):
            wp = (wp[1], -wp[0])
        else:
            wp = (-wp[1], wp[0])
    else:
        print(f"unknown {action}")

print(pos)
print(abs(pos[0]) + abs(pos[1]))
