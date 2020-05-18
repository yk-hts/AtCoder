n,t = map(int,input().split())
a = []
sum_t = t
for i in range(n):
    a.append(int(input()))

for i in range(1,n):
    if a[i] < a[i-1]+t :
        sum_t += (a[i]-a[i-1])
    else:
        sum_t += t
    
print(sum_t)