import math
N,M = map(int,input().split())

if abs(N-M) >= 2:
    print(0)
    exit()
sum = 1
count = 0
if N == M:
    sum *= N+M
    sum *= int(((N+M)/2))
    N = int((N+M)/2)-1
    M = N
else:
    sum *= max(N,M)

k = math.factorial(min(N,M))
sum *= k**2

print(sum%(10**9+7))

