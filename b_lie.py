n = int(input())
a,b = map(int,input().split())
k = int(input())
p = list(map(int,input().split()))

if a in p:
    print('NO')
elif b in p:
    print('NO')
elif len(p) != len(set(p)):
    print('NO')
else:
    print('YES')