from computer import compute
from collections import defaultdict

def print_board(board, sx, sy, d):
    for y in range(-50, 50):
        for x in range(-50, 50):
            if x == sx and y == sy:
                print(['^', '>', 'v', '<'][d], end='')        
            else:
                b = board.get((x, y), 0)
                print(' ' if b == 0 else '#', end='')
        print()
    print()

with open('input.txt') as f:
    xs = [int(x) for x in f.read().split(',')] + [0]*1000
    
count = 0

board = {(0, 0): 1}
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

print_board(board, x, y, d)