c = [list(map(str,input().split())) for i in range(4)]
z = []

for x in c:
    x.reverse()
    z.insert(0,x)

for a in z:
    print(*a)