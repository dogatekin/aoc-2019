from computer import compute
from collections import defaultdict

with open('input.txt') as f:
    xs = [int(x) for x in f.read().split(',')] + [0]*1000
    
count = 0

board = {}
x, y = 0, 0
d = 0

directions = {0: (0, -1),
              1: (1, 0),
              2: (0, 1),
              3: (-1, 0)}

out = None
i = 0
rel_base = 0
while True:
    out, xs, i, rel_base = compute(xs, board.get((x, y), 0), i, rel_base)

    if out is False:
        break
    
    paint, turn = out

    if (x, y) not in board:
        count += 1

    board[x, y] = paint

    t = [-1, 1][turn]
    d = (d + t) % 4
    dx, dy = directions[d]
    x += dx
    y += dy

print(count)