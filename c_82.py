N = int(input())
a = list(map(int,input().split()))
A = a.sort()
array = list(set(a))
array.sort()
sum = 0
n = 0
for i in range(len(array)):
    cnt = 0
    for j in range(n,len(a)):
        if array[i] == a[j]:
            cnt += 1
        else:
            break
    n += cnt
    if cnt >= array[i]:
        sum += cnt - array[i]
    else:
        sum += cnt
print(sum)