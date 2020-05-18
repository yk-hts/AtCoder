n,x = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,format(x,'b')))

b.reverse()
sum = 0
for i in range(len(b)):
    if b[i] == 1:
        sum += a[i]
print(sum)
# ans = sum(map(lambda x:x[0]*x[1],zip(a,b)))
# print(ans)