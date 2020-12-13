#!/usr/bin/python3
# P1
early = 1002392
buses = "23,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,37,x,x,x,x,x,421,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,17,x,19,x,x,x,x,x,x,x,x,x,29,x,487,x,x,x,x,x,x,x,x,x,x,x,x,13".split(',')

#early = 939
#buses = "7,13,x,x,59,x,31,19".split(',')

buses = [int(t) for t in buses if t != 'x']

times = {b: b - (early % b) for b in buses}

minbus = min(times, key=lambda k: times[k])

print(minbus * times[minbus])

# P2
buses = "23,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,37,x,x,x,x,x,421,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,17,x,19,x,x,x,x,x,x,x,x,x,29,x,487,x,x,x,x,x,x,x,x,x,x,x,x,13".split(',')
# All numbers are prime
#buses = "7,13,x,x,59,x,31,19".split(',')
# Find t, s.t. t % bus == add_to[t]
add_to = {int(bus): add for add, bus in enumerate(buses) if bus != 'x'}

t = 0
step = 1
for bus, add in add_to.items():
    while True:
        if (t + add) % bus == 0:
            step *= bus
            break
        t += step
print(t)
