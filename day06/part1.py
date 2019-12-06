from collections import defaultdict, deque

with open('input.txt', 'r') as f:
    xs = [x.strip() for x in f.readlines()]
    
orbits = defaultdict(list)

for x in xs:
    center, orbiting = x.split(')')
    orbits[center].append(orbiting)

q = deque([('COM', 0)])
total = 0
while q:
    obj, orbiting = q.popleft()
    total += orbiting
    for obj in orbits[obj]:
        q.append((obj, orbiting+1))
    
print(total)