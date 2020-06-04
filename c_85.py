N,Y = map(int,input().split())
sum = 0

for x in range(N+1):
    for y in range(N-x+1):
        z = N-x-y
        if x*1000+y*5000+z*10000 == Y:
            print(z,y,x)
            exit()
print(-1,-1,-1)
