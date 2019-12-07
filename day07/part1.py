from itertools import permutations
from collections import deque
from computer import compute

with open('input.txt', 'r') as f:
    xs = [int(x) for x in f.read().split(',')]

maximum = float('-inf')
for perm in permutations(range(5)):
    inp = 0
    for phase in perm:
        out, _, _ = compute(xs, deque([phase, inp]))
        inp = out
    maximum = max(out, maximum)
 
print(maximum)