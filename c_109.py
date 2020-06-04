from fractions import gcd
N,X = map(int,input().split())
x = list(map(int,input().split()))
x.append(X)
x.sort()
m = x[1]-x[0]

for i in range(1,N+1):
    n = x[i]-x[i-1]
    v = gcd(m,n)
    m = v

print(m)




