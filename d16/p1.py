#!/usr/bin/python3
with open('input') as f:
    lines = [x.strip() for x in f.readlines()]


# lines = """class: 1-3 or 5-7
# row: 6-11 or 33-44
# seat: 13-40 or 45-50
# 
# your ticket:
# 7,1,14
# 
# nearby tickets:
# 7,3,47
# 40,4,50
# 55,2,20
# 38,6,12""".splitlines()


parse_rules = True
your_ticket = False
nearby = False

all_rules = []
nearby_tickets = []

for line in lines:
    if parse_rules:
        if not line:
            parse_rules = False
            your_ticket = True
            continue
        rules = line.split(': ')[1]
        a1, a2 = rules.split(' or ')
        a11, a12 = a1.split('-')
        a21, a22 = a2.split('-')
        all_rules.append(((int(a11), int(a12)), (int(a21), int(a22))))

    elif your_ticket:
        if line.startswith('your'):
            continue
        if not line:
            your_ticket = False
            nearby = True
            continue
        my_ticket = list(int(x) for x in line.split(','))
    elif nearby:
        if line.startswith('nearby'):
            continue
        nearby_tickets.append(list(int(x) for x in line.split(',')))

print(all_rules)

def is_valid(val, rules):
    for r1, r2 in rules:
        if (r1[0] <= val <= r1[1]) or (r2[0] <= val <= r2[1]):
            return True
    return False

n = 0
print(nearby_tickets)
print('for t in nt')
for tick in nearby_tickets:
    print(tick)
    for val in tick:
        if not is_valid(val, all_rules):
            print(val)
            n += val
print(n)
