#!/usr/bin/python3
with open('input') as f:
    dirs = [(line[0], int(line[1:].strip())) for line in f.readlines()]

movement = {
    'N': (1, 0),
    'S': (-1, 0),
    'E': (0, 1),
    'W': (0, -1),
}

compass = {
    'N': 0,
    'S': 180,
    'E': 90,
    'W': 270,
}

undo_compass = {v: k for k, v in compass.items()}

pos = (0, 0)
facing = 'E'

for action, value in dirs:
    if action == "F":
        action = facing

    if action in movement:
        add = movement[action]
        pos = (pos[0] + value * add[0], pos[1] + value * add[1])
    elif action in 'LR':
        compass_dir = compass.get(facing)
        if action == 'L':
            scale = -1
        else:
            scale = 1
        compass_dir = (compass_dir + scale * value) % 360
        facing = undo_compass[compass_dir]        
    else:
        print(f"unknown {action}")

print(pos)
print(abs(pos[0]) + abs(pos[1]))
