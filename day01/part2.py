def fuel_for_mass(mass):
    total = 0
    fuel = mass//3 - 2
    
    while fuel > 0:
        total += fuel
        fuel = fuel//3 - 2
    
    return total

with open('input.txt') as f:
    lines = f.readlines()
    
masses = [int(line.strip()) for line in lines]

print(sum(fuel_for_mass(mass) for mass in masses))
