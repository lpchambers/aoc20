#!/usr/bin/python3
inp = "469217538"
#inp = "389125467"


class Node:
    def __init__(self, val, prev):
        self.val = val
        self.prev = prev
        if prev:
            prev.next = self
        self.next = None

    def set_prev(self, p):
        self.prev = p

    def set_next(self, n):
        self.next = n

    def search(self, n):
        """Return node"""
        cur = self
        while cur is not None:
            if cur.val == n:
                return cur
            cur = cur.next

    def print(self):
        n = self.next
        print(self.val, end="")
        while n != self:
            print(n.val, end="")
            n = n.next
        print()

N = 1000000

nodes = {}

prev = None
for x in inp:
    node = Node(int(x), prev)
    nodes[node.val] = node
    if x == inp[0]:
        cur = node
    prev = node


for x in range(len(inp)+1, N+1):
    prev = Node(x, prev)
    nodes[prev.val] = prev

prev.set_next(cur)
cur.set_prev(prev)

MAX = N
print(MAX)

for _ in range(10*1000*1000):
    pick0 = cur.next
    pick1 = cur.next.next.next
    after = pick1.next

    pick0.set_prev(None)
    pick1.set_next(None)
    cur.set_next(after)
    after.set_prev(cur)

    pick_vals = [pick0.val, pick0.next.val, pick1.val]

    target = cur.val - 1 % MAX
    if target == 0:
        target = MAX
    while target in pick_vals:
        target = (target - 1) % MAX
        if target == 0:
            target = MAX

    target = nodes[target]
    target_after = target.next
    target.set_next(pick0)
    pick0.set_prev(target)
    target_after.set_prev(pick1)
    pick1.set_next(target_after)

    # Move cursor
    cur = cur.next
    if (_ % 1000000) == 0:
        print("YAY")


one = nodes[1]
print(one.next.val, one.next.next.val)
print(one.next.val * one.next.next.val)
