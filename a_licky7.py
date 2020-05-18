n = int(input())
n1 = str(n)
for i in range(len(n1)):
    if n1[i] == '7':
        print('Yes')
        break
    if i == len(n1)-1:
        print('No')
