from itertools import permutations
from computer import compute

with open('input.txt', 'r') as f:
    xs = [int(x) for x in f.read().split(',')]
    
# xs = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]

maximum = float('-inf')
for perm in permutations(range(5)):
    inp = 0
    for phase in perm:
        out = compute(xs, [inp, phase])
        inp = out
    maximum = max(out, maximum)
 
print(maximum)