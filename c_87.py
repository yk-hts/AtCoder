N = int(input())
A = [list(map(int,input().split())) for _ in range(2)]
ans = []
max = 0
for i in range(1,N):
    s = sum(A[0][0:i])+sum(A[1][i-1:N])
    if s > max:
        max = s

if N == 1:
    print(A[0][0]+A[1][0])
else:
    print(max)