N = int(input())
a = [int(input()) for _ in range(N)]

a.sort()
sum_a = sum(a)
d = sum_a

for i in range(N):
    if a[i]%10 != 0:
        d = a[i]
        break

if sum_a%10 != 0:
    ans = sum_a
else:
    ans = sum_a-d

print(ans)