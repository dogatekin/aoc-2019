from collections import Counter

with open('input.txt', 'r') as f:
    xs = f.read()

layer_size = 6 * 25
layers = [xs[i:i+layer_size] for i in range(0, len(xs), layer_size)]
counts = [Counter(layer) for layer in layers]

min_zeros = min(counts, key=lambda c: c['0'])

print(min_zeros['1'] * min_zeros['2'])