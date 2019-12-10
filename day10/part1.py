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
print(best, detects[best])