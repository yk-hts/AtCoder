import collections
N = int(input())
a = list(map(int,input().split()))
cnt = 0
ans = []
item = []
for i in range(N):
    ans.append(a[i]-1)
    ans.append(a[i])
    ans.append(a[i]+1)

c = collections.Counter(ans)
d = c.most_common()

# for i in range(N):
#     for j in range(N):
#         item.append(a[i][j])



print(d[0][1])