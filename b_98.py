N = int(input())
S = list(input())
cnt = []
for i in range(0,N):
    s1 = set(S[0:i])
    s2 = set(S[i:])
    cnt.append(len(list(s1 & s2)))
print(max(cnt))
