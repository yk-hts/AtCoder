n = int(input())
z = []

for i in range(n):
    p = list(map(int,input().split()))
    z.append(p)

for i in range(n):
    if z[i][0] < z[i][1]+z[i][2]:
        print('No')
        exit()
    elif z[i][0]%2==0:
        if (z[i][1]+z[i][2])%2 != 0:
            print('No')
            exit()
    elif z[i][0]%2==1:
        if (z[i][1]+z[i][2])%2 != 1:
            print('No')
            exit()

print('Yes')