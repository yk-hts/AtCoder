n = int(input())

count = 0
array = []
if n%2!=0:
    count = 1
    n -= 1
    array.append(1)
while(n > 1):
        count += 1
        n -= 2
        array.append(2)
print(count)
for i in range(len(array)):
    print(array[i])