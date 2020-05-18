n,m = map(int,input().split())
a = list(map(int,input().split()))
a_sum = sum(a)

list.sort(a,reverse=True)
judge = 1

for i in range(m):
    if a[i]< a_sum*1/(m*4):
        judge = 0
        break

if judge == 0:
    print('No')
else:
    print('Yes')