a,b = map(str,input().split())
for i in range(1,100100):
    if int(a+b) == i**2:
        print('Yes')
        exit()

print('No')