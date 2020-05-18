import math
n = int(input())
r = []
count = 0
sum_r = 0
for i in range(n):
    r.append(int(input()))
r.sort()

for i in range(n-1,-1,-1):
    if count%2==0:
        sum_r += r[i]**2
    else:
        sum_r -= r[i]**2
    count += 1
print(sum_r*math.pi)