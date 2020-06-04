N = int(input())
s = []
t = []
for i in range(N):
    s.append(input())
M = int(input())
for i in range(M):
    t.append(input())

S = set(s)
ans = []
for i in S:
    cnt = 0
    for j in s:
        if i == j:
            cnt += 1
    for h in t:
        if i == h:
            cnt -= 1
    ans.append(cnt)

value = max(ans)

if value < 0:
    print(0)
else:
    print(value)