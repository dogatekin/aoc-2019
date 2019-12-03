from computer import compute

with open('input.txt', 'r') as f:
    xs = [int(x) for x in f.read().split(',')]
    
xs[1] = 12
xs[2] = 2

print(compute(xs)[0])