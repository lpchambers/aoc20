#!/usr/bin/python3
import copy
with open('input') as f:
    lines = [x.strip() for x in f.readlines()]


# lines = """class: 0-1 or 4-19
# row: 0-5 or 8-19
# seat: 0-13 or 16-19
# 
# your ticket:
# 11,12,13
# 
# nearby tickets:
# 3,9,18
# 15,1,5
# 5,14,9
# 100,1,2""".splitlines()

parse_rules = True
your_ticket = False
nearby = False

all_rules = []
nearby_tickets = []

dep_index = []

for idx, line in enumerate(lines):
    if parse_rules:
        if not line:
            parse_rules = False
            your_ticket = True
            continue
        if 'departure' in line:
            dep_index.append(idx)
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


def is_valid(val, rules):
    for r1, r2 in rules:
        if (r1[0] <= val <= r1[1]) or (r2[0] <= val <= r2[1]):
            return True
    return False

valid_tickets = []

for tick in nearby_tickets:
    for val in tick:
        if not is_valid(val, all_rules):
            break
    else:
        valid_tickets.append(tick)


nfields = len(valid_tickets[0])

ticket_index_to_rule_index = {}


test_rules = copy.deepcopy(all_rules)

for rule in all_rules:
    print(rule)
print(len(valid_tickets))
print(len(nearby_tickets))

untested = list(range(nfields))

while len(untested) != 0:
    for field in untested:
        valid_rules = copy.deepcopy(test_rules)
        #print(f"field {field}")
        for tick in valid_tickets:
            val = tick[field]
            #print(f"  val {val}")
            valid_rules = [rule for rule in valid_rules if is_valid(val, [rule])]
            #print(f"    LEN {len(valid_rules)}")
            if len(valid_rules) == 1:
                ticket_index_to_rule_index[field] = all_rules.index(valid_rules[0])
                test_rules.remove(valid_rules[0])
                untested.remove(field)
                break
    print(ticket_index_to_rule_index)

rule_index_to_ticket_index = {v: k for k, v in ticket_index_to_rule_index.items()}
print(dep_index)
tick_dep_indexes = [rule_index_to_ticket_index[idx] for idx in dep_index]
print(tick_dep_indexes)
prod = 1
for idx in tick_dep_indexes:
    prod *= my_ticket[idx]

print(prod)
