from computer import compute

with open('input.txt', 'r') as f:
    xs = [int(x) for x in f.read().split(',')]

target = 19690720

for noun in range(99):
    for verb in range(99):
        initial = xs.copy()
        initial[1] = noun
        initial[2] = verb
        
        if compute(initial)[0] == target:
            print(100*noun + verb)