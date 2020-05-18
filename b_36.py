N = int(input())
S = []
ans = []

for i in range(N):
    s = list(input())
    S.append(s)

for i in range(N):
    s = []
    for j in range(N):
        s.append(S[N-1-j][i])
    print(''.join(s))
