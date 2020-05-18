# N,M = map(int,input().split())
# H = list(map(int,input().split()))
# ans = [1]*N

# for i in range(M):
#     a,b = map(int,input().split())
#     if H[a-1] <= H[b-1]:
#         ans[a-1] -= ans[a-1]
#     if H[a-1] >= H[b-1]:
#         ans[b-1] -= ans[b-1]

# print(sum(ans))

n, m = map(int, input().split())
h = list(map(int, input().split()))
a, b = [0] * m, [0] * m
data = [[] for _ in range(n)]
for i in range(m):
    a[i], b[i] = map(int, input().split())
    data[a[i] - 1].append(b[i] - 1)
    data[b[i] - 1].append(a[i] - 1)
    print(data)
ans = 0
for i in range(n):
    flag = True
    for x in data[i]:
        if h[i] <= h[x]:
            flag = False
            break
    if flag:
        ans += 1
print(ans)

