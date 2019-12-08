with open('input.txt', 'r') as f:
    xs = f.read()

layer_size = 6 * 25
layers = [xs[i:i+layer_size] for i in range(0, len(xs), layer_size)]

image = []
for i in range(len(layers[0])):
    for layer in layers:
        if layer[i] == '2':
            continue
        image.append(layer[i])
        break
        
for i, pxl in enumerate(image):
    if i > 0 and i % 25 == 0:
        print()
    
    print('||' if pxl == '1' else '  ', end='')
