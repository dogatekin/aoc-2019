import re
from math import gcd

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

with open('input.txt') as f:
    moons = f.readlines()

dimensions = 3
cur_lcm = 1

for d in range(dimensions):
    positions = [list(map(int, re.search(r'<x=(.*), y=(.*), z=(.*)>', moon).groups())) for moon in moons]
    velocities = [[0]*dimensions for _ in range(len(positions))]

    tup_pos = tuple(pos[d] for pos in positions)
    tup_vel = tuple(vel[d] for vel in velocities)  

    seen = {tup_pos + tup_vel}
    step = 1
    while True:
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
        
        tup_pos = tuple(pos[d] for pos in positions)
        tup_vel = tuple(vel[d] for vel in velocities)  
        tup = tup_pos + tup_vel  
        if tup in seen:
            break
        
        seen.add(tup)
        step += 1
    
    cur_lcm = lcm(cur_lcm, step)

print(cur_lcm)
    