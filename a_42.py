A,B,C = map(int,input().split())
count7 = 0
count5 = 0

ans = [A,B,C]

for i in ans:
    if i == 7:
        count7 += 1
    elif i == 5:
        count5 += 1

if count7 == 1 and count5 == 2:
    print('YES')
else:
    print('NO')