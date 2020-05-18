n,k = map(int,input().split())

n = n%k

if n<abs(n-k):
    print(n)
else:
    print(abs(n-k))