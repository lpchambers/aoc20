#!/usr/bin/python3
with open('input') as f:
    lines = f.readlines()

bag_contains = {}

for line in lines:
    if 'no other bags' in line:
        bag = line.split(' bags')[0]
        bag_contains[bag] = []
        continue

    bag, contents = line.split(' bags contain ')
    inside = []
    for content in contents.split(','):
        nice_content = content.strip().split(' bag')[0]
        n, *name = nice_content.split()
        bag_name = " ".join([*name])
        n = int(n)
        inside.append((n, bag_name))
    bag_contains[bag] = inside



hold_shiny = ['shiny gold']
n = 0

while n != len(hold_shiny):
    n = len(hold_shiny)
    for bag, contents in bag_contains.items():
        if bag in hold_shiny:
            continue
        for nbags, inside_name in contents:
            if any(x in inside_name for x in hold_shiny):
                hold_shiny.append(bag)
                break

print(len(hold_shiny) - 1)

n_holds = {}

def get_n_holds(bag):
    if bag in n_holds:
        return n_holds[bag]
    bags_in = 0
    for n, subbag in bag_contains[bag]:
        bags_in += (n + n * get_n_holds(subbag))

    n_holds[bag] = bags_in
    return bags_in

print(get_n_holds('shiny gold'))
