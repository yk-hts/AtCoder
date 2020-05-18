n,y = map(int,input().split())

for i in range(n+1):
    for j in range(n+1-i):
        h = n-i-j
        if i*10000+j*5000+h*1000 == y:
            print(i,j,h)
            exit()
print(-1,-1,-1)


