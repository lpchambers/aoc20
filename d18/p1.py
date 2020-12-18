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
        if len(stack) == 3:
            if stack[1] == '+':
                stack = [stack[0] + stack[2]]
            elif stack[1] == '*':
                stack = [stack[0] * stack[2]]
        print("stack", stack)

    return stack[0]


#print(solve("1 + 2 * 3 + 4 * 5 + 6"))
#print(solve("1 + (2 * 3) + (4 * (5 + 6))"))

n = 0
for line in lines:
    n += solve(line)
print(n)
