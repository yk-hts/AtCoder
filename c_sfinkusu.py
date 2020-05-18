N, M = map(int, input().split())
 
for c in range(N+1):
    b = M-2*N-2*c
    a = N-b-c
    if b >= 0 and a >= 0:
        print(a,b,c)
        exit()
print(-1, -1, -1)