w = input()

while len(w)>0:
    if w[-5:] == 'dream':
        w = w[:-5]
    elif w[-7:] == 'dreamer':
        w = w[:-7]
    elif w[-5:] == 'erase':
        w = w[:-5]
    elif w[-6:] == 'eraser':
        w = w[:-6]
    else:
        print('NO')
        exit()
print('YES')
