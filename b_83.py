N,A,B = map(int,input().split())
sum = 0
array = []
for i in range(1,N+1):
    array.append(list(str(i)))

for i in range(N):
    value = 0
    for j in range(len(array[i])):
        value += int(array[i][j])
    if A <= value <= B:
        sum += int(''.join(array[i]))
print(sum)        

