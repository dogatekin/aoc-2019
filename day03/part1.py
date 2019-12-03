def closest_x(a, b):
    central_port = (0, 0)
    
    directions = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
    
    points_a = set()
    intersections = []
    
    x, y = central_port
    for piece in a:
        direction, distance = piece[0], int(piece[1:])
        dx, dy = directions[direction]
        for _ in range(distance):
            x += dx
            y += dy
            points_a.add((x, y))

    x, y = central_port
    for piece in b:
        direction, distance = piece[0], int(piece[1:])
        dx, dy = directions[direction]
        for _ in range(distance):
            x += dx
            y += dy
            if (x, y) in points_a:
                intersections.append(abs(x) + abs(y))
    
    return min(intersections)

assert closest_x(['R8','U5','L5','D3'], ['U7','R6','D4','L4']) == 6
assert closest_x(['R75','D30','R83','U83','L12','D49','R71','U7','L72'], ['U62','R66','U55','R34','D71','R55','D58','R83']) == 159
assert closest_x(['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'], ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']) == 135

with open('input.txt', 'r') as f:
    lines = f.readlines()

a, b = (line.strip().split(',') for line in lines)

print(closest_x(a, b))