def get(xs, i, mode):
    if mode == '0':
        return xs[xs[i]]
    elif mode == '1':
        return xs[i]

def compute(xs, inputs, i=0):
    ins = xs[i]
    op = str(ins)[-2:]
    modes = str(ins)[-3::-1]
    modes = modes + '0'*(2-len(modes))
    out = None
    
    while op != '99':
        if op.endswith('1'):
            xs[xs[i+3]] = get(xs, i+1, modes[0]) + get(xs, i+2, modes[1])
            i += 4
        elif op.endswith('2'):
            xs[xs[i+3]] = get(xs, i+1, modes[0]) * get(xs, i+2, modes[1])
            i += 4
        elif op.endswith('3'):
            if out is not None:
                return out, xs, i
            xs[xs[i+1]] = inputs.popleft()
            i += 2
        elif op.endswith('4'):
            out = get(xs, i+1, modes[0])
            i += 2
        elif op.endswith('5'):
            if get(xs, i+1, modes[0]):
                i = get(xs, i+2, modes[1])
            else:
                i += 3
        elif op.endswith('6'):
            if not get(xs, i+1, modes[0]):
                i = get(xs, i+2, modes[1])
            else:
                i += 3
        elif op.endswith('7'):
            if get(xs, i+1, modes[0]) < get(xs, i+2, modes[1]):
                xs[xs[i+3]] = 1
            else:
                xs[xs[i+3]] = 0
            i += 4
        elif op.endswith('8'):
            if get(xs, i+1, modes[0]) == get(xs, i+2, modes[1]):
                xs[xs[i+3]] = 1
            else:
                xs[xs[i+3]] = 0
            i += 4
        else:
            raise IndexError
        
        ins = xs[i]
        op = str(ins)[-2:]
        modes = str(ins)[-3::-1]
        modes = modes + '0'*(2-len(modes))
    
    return out, xs, i