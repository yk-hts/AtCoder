N = int(input())
a = [int(input()) for _ in range(N)]
count = 1
value = 1

for i in range(len(a)):
    if a[value-1] == 2:
        break
    value = a[value-1]
    count += 1

if count > len(a):
    count = -1

print(count)