n = int(input())
a = list(map(int,input().split()))
sum = 0
for i in range(1,n+1):
    if i%2 == 1:
        sum += max(a)
    else:
        sum -= max(a)
    a[a.index(max(a))] = 0
print(sum)