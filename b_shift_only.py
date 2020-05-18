n = int(input())
a = list(map(int,input().split()))

judge = 0
count = 0

while judge != 1:
    for i in range(n):
        if a[i]%2 != 0:
            judge = 1
            break
        else:
            a[i] /=2
    count += 1
print(count-1)