from computer import compute
from collections import Counter

with open('input.txt') as f:
    xs = [int(x) for x in f.read().split(',')] + [0]*1000
    
out, _, _, _ = compute(xs)

w = max(out[::3]) + 1
h = max(out[1::3]) + 1
board = [[0]*w for _ in range(h)]

for i in range(0, len(out), 3):
    x, y, t = out[i:i+3]
    board[y][x] = t
    
row_counts = [Counter(row) for row in board]
print(sum(count[2] for count in row_counts))