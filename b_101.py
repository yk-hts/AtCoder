N = list(input())
sum = 0
for i in N:
    sum += int(i)

if int(''.join(N))%sum == 0:
    print('Yes')
else:
    print('No')
