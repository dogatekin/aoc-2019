from itertools import permutations
from collections import deque
from computer import compute

with open('input.txt', 'r') as f:
    XS = [int(x) for x in f.read().split(',')]
    
maximum = float('-inf')
for perm in permutations(range(5, 10)):
    states = [(XS[:], deque([phase]), 0) for phase in perm]
    states[0][1].append(0)

    while states[-1][0][states[-1][2]] != 99:
        for i in range(len(states)):
            xs, inputs, ip = states[i]
            out, xs_new, ip_new = compute(xs, inputs, ip)
            states[i] = (xs_new, deque(), ip_new)
            
            states[(i+1) % len(states)][1].append(out)

    maximum = max(out, maximum)
    
print(maximum)