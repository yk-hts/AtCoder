N = int(input())
T = list(map(int,input().split()))
M = int(input())
P = []
X = []

for i in range(M):
    p,x = map(int,input().split())
    P.append(p)
    X.append(x)

for i in range(M):
    T2 = T.copy()
    T2[P[i]-1] = X[i]
    print(sum(T2))
