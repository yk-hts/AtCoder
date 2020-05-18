n = int(input())
a = [int(input()) for i in range(n)]
max_a = max(a)
for i in range(n):
    if a[i] == max_a:
        a[i] = 0
print(max(a))