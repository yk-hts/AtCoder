l = list(map(int,input().split()))
l.sort()
if l.count(l[0]) == 1:
    print(l[0])
else:
    print(l[2])


