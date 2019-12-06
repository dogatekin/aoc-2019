from collections import defaultdict, deque

with open('input.txt', 'r') as f:
    xs = [x.strip() for x in f.readlines()]
    
orbits = defaultdict(list)

for x in xs:
    center, orbiting = x.split(')')
    orbits[center].append(orbiting)
    orbits[orbiting].append(center)
    
q = deque([('YOU', 0)])
seen = set()
while q:
    obj, steps = q.popleft()

    if obj == 'SAN':
        print(steps-2)
        
    seen.add(obj)
    for neighbor in orbits[obj]:
        if neighbor not in seen:
            q.append((neighbor, steps+1))
    
