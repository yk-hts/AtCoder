s = int(input())
array = [s]
i = 0
flag = True
while flag:
    x = 0
    if array[i]%2==0:
        x = array[i]//2
    else:
        x = 3*array[i]+1
    if x in array:
        print(i+2)
        flag = False
    else:
        array.append(x)
        i += 1
    