n,a,b = map(int,input().split())
sum = 0
array = [str(x) for x in range(1,n+1)]
for i in range(n):
    sum_i = 0
    for j in range(len(array[i])):
        sum_i += int(array[i][j])
    if(sum_i <= b and sum_i >= a):
        sum += int(array[i])
print(sum)