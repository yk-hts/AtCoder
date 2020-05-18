import math
a,b,n = map(int,input().split())
ans = []
for i in range(n,-1,-1):
    ans.append(math.floor(a*i/b)-a*math.floor(i/b))
print(max(ans))