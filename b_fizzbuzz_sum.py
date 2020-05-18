n = int(input())
array = list([x+1 for x in range(n)] if (x+1)%15!=0 and )
sum = 0
for i in range(len(array)):
    if array[i]%15==0:
        array[i] = 'fizzbuzz'
    elif array[i]%3==0:
        array[i] = 'fizz'
    elif array[i]%5==0:
        array[i] = 'buzz'
    else:
        sum += array[i]


print(sum)