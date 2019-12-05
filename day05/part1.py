from computer import compute

with open('input.txt', 'r') as f:
    xs = [int(x) for x in f.read().split(',')]
    
compute(xs)