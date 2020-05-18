W,H,N = map(int,input().split())
X = [i for i in range(W+1)]
Y = [i for i in range(H+1)]

for i in range(N):
    x,y,a = map(int,input().split())
    if a == 1:
        for j in range(W+1):
            if X[j] < x:
                X[j] = x
    elif a == 2:
        for j in range(W+1):
            if X[j] > x:
                X[j] = x
    elif a == 3:
        for j in range(H+1):
            if Y[j] < y:
                Y[j] = y
    else:
        for j in range(H+1):
            if Y[j] > y:
                Y[j] = y
print((max(X)-min(X))*(max(Y)-min(Y)))