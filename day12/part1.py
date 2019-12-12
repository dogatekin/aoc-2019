import re

with open('input.txt') as f:
    moons = f.readlines()

positions = [list(map(int, re.search(r'<x=(.*), y=(.*), z=(.*)>', moon).groups())) for moon in moons]

dimensions = 3
velocities = [[0]*dimensions for _ in range(len(positions))]

for step in range(1000):
    gravities = [[0]*dimensions for _ in range(len(positions))]
    
    for i in range(len(positions)):
        for j in range(i+1, len(positions)):
            this = positions[i]
            other = positions[j]
            
            for dim in range(dimensions):
                if this[dim] < other[dim]:
                    gravities[i][dim] += 1
                    gravities[j][dim] -= 1
                elif this[dim] > other[dim]:
                    gravities[i][dim] -= 1
                    gravities[j][dim] += 1

    for i in range(len(positions)):
        for dim in range(dimensions):
            velocities[i][dim] += gravities[i][dim]
            positions[i][dim] += velocities[i][dim]

pots = [sum(map(abs, pos)) for pos in positions]
kins = [sum(map(abs, vel)) for vel in velocities]
e = sum(pot*kin for pot, kin in zip(pots, kins))
print(e)
    