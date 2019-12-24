from computer import compute

def print_area(explored):
    min_x = (min(explored.keys(), key=lambda pos: pos[0]))[0]
    min_y = (min(explored.keys(), key=lambda pos: pos[1]))[1]
    
    max_x = (max(explored.keys(), key=lambda pos: pos[0]))[0]
    max_y = (max(explored.keys(), key=lambda pos: pos[1]))[1]
    
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            if (x, max_y-y+min_y) in explored:
                print(explored[(x, max_y-y+min_y)], end='')
            else:
                print(' ', end='')
        print()
                

def explore(xs, d, ip, rel_base, explored, pos, step):
    out, new_xs, new_ip, new_rel_base = compute(xs, d, ip, rel_base)
    
    x, y = pos
    dx, dy = ((0, 1), (0, -1), (-1, 0), (1, 0))[d-1]
    new_pos = (x+dx, y+dy)
    
    if new_pos in explored:
        return
    
    if out == 0:
        explored[new_pos] = '#'
    else:
        if out == 1:
            explored[new_pos] = '.'
        else:
            explored[new_pos] = '@'
        
        for val in range(1, 5):
            explore(new_xs, val, new_ip, new_rel_base, explored, new_pos, step+1)


with open('input.txt') as f:
    xs = [int(x) for x in f.read().split(',')] + [0]*1000
 
explored = {(0, 0): 'D'}
ip = rel_base = 0

for d in range(1, 5):
    explore(xs, d, ip, rel_base, explored, (0, 0), 1)

oxygen = [key for key in explored if explored[key] == '@'][0]

def oxygenate(area, d, pos, step=1):
    x, y = pos
    dx, dy = ((0, 1), (0, -1), (-1, 0), (1, 0))[d-1]
    new_pos = (x+dx, y+dy)
    
    if area[new_pos] in ['O', '#']:
        return step-1
    else:
        area[new_pos] = 'O'
        return max(oxygenate(area, d, new_pos, step+1) for d in range(1, 5))
            
print(max(oxygenate(explored, d, oxygen) for d in range(1, 5)))