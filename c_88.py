c = [list(map(int,input().split())) for i in range(3)]
a1 = 0
a2 = 0
a3 = 0
b1 = 0
b2 = 0
b3 = 0
m = min(c[0])
for i in range(m+1):
    a1 = i
    b1 = c[0][0]-a1
    b2 = c[0][1]-a2
    b3 = c[0][2]-a3
    if c[1][0]-b1 == c[1][1]-b2 == c[1][2]-b3:
        a2 = c[1][0]-b1
    else:
        continue
    if c[2][0]-b1 == c[2][1]-b2 == c[2][2]-b3:
        print('Yes')
        exit()
print('No')


