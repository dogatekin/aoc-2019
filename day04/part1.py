count = 0
for x in range(234208, 765869+1):
    s = str(x)
    adj = False
    dec = False
    for i in range(len(s)-1):
        d1 = s[i]
        d2 = s[i+1]
        
        if d1 == d2:
            adj = True
        if d1 > d2:
            dec = True
    
    if adj and not dec:
        count += 1

print(count)