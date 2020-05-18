n = int(input())
a = list(map(int,input().split()))
avg = sum(a)/n
count = 0

if sum(a)%n != 0:
    print(-1)
    exit()

for i in range(len(a)-1):
    if sum(a[0:i+1]) != len(a[0:i+1])*avg or sum(a[i+1:len(a)]) != len(a[i+1:len(a)])*avg:
        count += 1
print(count)

