import subprocess as sp
from computer import compute
from collections import Counter
from getch import getch

def display(board, tiles, score):
    for row in board:
        for tile in row:
            print(tiles[tile], end='')
        print()
    print(f'Score: {score}')
    
with open('input.txt') as f:
    xs = [int(x) for x in f.read().split(',')] + [0]*10000

xs[0] = 2
 
tiles = {
    0: ' ',
    1: '░',
    2: '#',
    3: '▆',
    4: 'O'
}

w = 37
h = 20
board = [[0]*w for _ in range(h)]
score = 0
inp = None
ip = 0
rel_base = 0

while True:
    out, new_xs, new_ip, new_rel_base = compute(xs, inp, ip, rel_base)

    for i in range(0, len(out), 3):
        x, y, t = out[i:i+3]

        if x == -1 and y == 0:
            score = t
        else:
            board[y][x] = t

    sp.call('clear', shell=True)
    display(board, tiles, score)
    
    char = getch()
    if char == 'z':
        xs, ip, rel_base = old_xs, old_ip, old_rel_base
    else:
        inp = {' ': 0, 'a': -1, 'd': 1}[char]
        
        old_xs, old_ip, old_rel_base = xs, ip, rel_base
        xs, ip, rel_base = new_xs, new_ip, new_rel_base
        
        if xs[ip] == 99:
            break
