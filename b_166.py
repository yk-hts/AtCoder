n,k = map(int,input().split())
ans = [i for i in range(1,n+1)]
for i in range(k):
    d = int(input())
    a = list(map(int,input().split()))
    for j in a:
        if j in ans:
            del ans[(ans.index(j))]
print(len(ans))

