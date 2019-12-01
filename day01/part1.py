with open('input.txt') as f:
    lines = f.readlines()
    
masses = [int(line.strip()) for line in lines]

fuel = sum(mass//3 - 2 for mass in masses)

print(fuel)