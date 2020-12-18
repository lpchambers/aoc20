#!/usr/bin/python3
with open('input') as f:
    lines = [x.strip() for x in f.readlines()]


def find_matching_bracket(line, idx):
    print("find_match idx:", idx, "line", line)
    depth = 1
    idx = idx + 1
    while depth > 0:
        c = line[idx]
        if c == '(':
            depth += 1
        elif c == ')':
            depth -= 1
        idx += 1
    return idx


def solve(line):
    stack = []
    idx = 0
    print("solve", line)
    while idx < len(line):
        c = line[idx]
        if c == '(':
            end_idx = find_matching_bracket(line, idx)
            # Ignore both brackets now
            bracket_solved = solve(line[idx + 1: end_idx - 1])
            stack.append(bracket_solved)
            idx = end_idx + 1
        elif c == " ":
            idx += 1
        elif c in ['*', '+']:
            stack.append(c)
            idx += 1
        else:
            stack.append(int(c))
            idx += 1
    # Try to apply stack
    print("stack", stack)
    while len(stack) > 1:
        if '+' in stack:
            add_idx = stack.index('+') - 1
            before = stack.pop(add_idx)
            stack.pop(add_idx)
            after = stack.pop(add_idx)
            stack.insert(add_idx, before + after)
        else:
            add_idx = stack.index('*') - 1
            before = stack.pop(add_idx)
            stack.pop(add_idx)
            after = stack.pop(add_idx)
            stack.insert(add_idx, before * after)
        print("stack", stack)

    return stack[0]


# print(solve("1 + 2 * 3 + 4 * 5 + 6"))
# print(solve("1 + (2 * 3) + (4 * (5 + 6))"))
# print(solve("5 + (8 * 3 + 9 + 3 * 4 * 3)"))

n = 0
for line in lines:
    n += solve(line)
print(n)
