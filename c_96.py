H,W = map(int,input().split())

s=[list(str(input())) for _ in range(H)]

di=[1,-1,0,0]
dj=[0,0,1,-1]
for i in range(H):
    for j in range(W):
        if s[i][j]=='#':
            found=False
            for k in range(4):
                i2=i+di[k]
                j2=j+dj[k]
                if 0<=i2 and i2<H and 0<=j2 and j2<W:
                    if s[i2][j2]=='#':
                        found=True
            if not found:
                print('No')
                exit()

print('Yes')


