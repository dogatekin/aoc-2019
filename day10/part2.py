from collections import defaultdict, OrderedDict
from itertools import cycle

def sign(x):
    return -1 if x < 0 else 1


def line(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    
    direction = (sign(x2 - x1), sign(y2 - y1))
    
    if x1 == x2:
        return (float('inf'), 0, direction)
    if y1 == y2:
        return (0, y1, direction)
    
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m*x1
    
    return (m, b, direction)  


def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    
    return (y2-y1)**2 + (x2-x1)**2


with open('input.txt', 'r') as f:
    ast_map = [line.strip() for line in f.readlines()]
    
asteroids = set()

for y, row in enumerate(ast_map):
    for x, c in enumerate(row):
        if c == '#':
            asteroids.add((x, len(ast_map)-1-y))

detects = {}
for asteroid in asteroids:
    lines_of_sight = set()
    for other in asteroids - {asteroid}:
        lines_of_sight.add(line(asteroid, other))
    detects[asteroid] = len(lines_of_sight)
    
best = max(detects, key=detects.get)

q1 = defaultdict(list)
q2 = defaultdict(list)
q3 = defaultdict(list)
q4 = defaultdict(list)
for other in asteroids - {best}:
    m, _, drc = line(best, other)
    d = dist(best, other)
    if drc == (1,1):
        q1[m].append((other, d))
    elif drc == (1,-1):
        q2[m].append((other, d))
    elif drc == (-1,-1):
        q3[m].append((other, d))
    elif drc == (-1,1):
        q4[m].append((other, d))

num = 0
for q in cycle((q1, q2, q3, q4)):
    targets = OrderedDict(sorted(q.items(), reverse=True))
    for m, asts in targets.items(): 
        asts.sort(key=lambda t: t[1], reverse=True)
        if asts:
            num += 1
            destroyed = asts.pop()
            x, y = destroyed[0]
            if num == 200:
                print(num, (x, len(ast_map)-1-y))
                break
    
    if num == len(asteroids)-1 or num == 200:
        break
