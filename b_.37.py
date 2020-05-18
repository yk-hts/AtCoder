N,Q = map(int,input().split())
array = []
a = [0]*N

for i in range(Q):
    L,R,T = map(int,input().split())
    array.append([L,R,T])

for i in array:
    L = i[0]
    R = i[1]
    T = i[2]
    for j in range(L-1,R):
        a[j] = T

for i in a:
    print(i)

