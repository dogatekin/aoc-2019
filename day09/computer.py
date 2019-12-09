def get(xs, i, mode, rel_base):
    if mode == '0':
        return xs[i]
    elif mode == '1':
        return i
    elif mode == '2':
        return rel_base + xs[i]

def compute(xs, inp, i=0):
    ins = xs[i]
    op = str(ins)[-2:]
    modes = str(ins)[-3::-1]
    modes = modes + '0'*(3-len(modes))
    rel_base = 0
    
    while op != '99':
        if op.endswith('1'):
            xs[get(xs, i+3, modes[2], rel_base)] = xs[get(xs, i+1, modes[0], rel_base)] + xs[get(xs, i+2, modes[1], rel_base)]
            i += 4
        elif op.endswith('2'):
            xs[get(xs, i+3, modes[2], rel_base)] = xs[get(xs, i+1, modes[0], rel_base)] * xs[get(xs, i+2, modes[1], rel_base)]
            i += 4
        elif op.endswith('3'):
            xs[get(xs, i+1, modes[0], rel_base)] = inp
            i += 2
        elif op.endswith('4'):
            print(xs[get(xs, i+1, modes[0], rel_base)])
            i += 2
        elif op.endswith('5'):
            if xs[get(xs, i+1, modes[0], rel_base)]:
                i = xs[get(xs, i+2, modes[1], rel_base)]
            else:
                i += 3
        elif op.endswith('6'):
            if not xs[get(xs, i+1, modes[0], rel_base)]:
                i = xs[get(xs, i+2, modes[1], rel_base)]
            else:
                i += 3
        elif op.endswith('7'):
            if xs[get(xs, i+1, modes[0], rel_base)] < xs[get(xs, i+2, modes[1], rel_base)]:
                xs[get(xs, i+3, modes[2], rel_base)] = 1
            else:
                xs[get(xs, i+3, modes[2], rel_base)] = 0
            i += 4
        elif op.endswith('8'):
            if xs[get(xs, i+1, modes[0], rel_base)] == xs[get(xs, i+2, modes[1], rel_base)]:
                xs[get(xs, i+3, modes[2], rel_base)] = 1
            else:
                xs[get(xs, i+3, modes[2], rel_base)] = 0
            i += 4
        elif op.endswith('9'):
            rel_base += xs[get(xs, i+1, modes[0], rel_base)]
            i += 2
        else:
            raise IndexError
        
        ins = xs[i]
        op = str(ins)[-2:]
        modes = str(ins)[-3::-1]
        modes = modes + '0'*(3-len(modes))