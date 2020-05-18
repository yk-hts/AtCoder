n,s,t = map(int,input().split())
w = 0
count = 0
for i in range(n):
    w += int(input())
    if s <= w <= t:
        count += 1
print(count)