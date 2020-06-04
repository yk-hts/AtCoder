A,B,X = map(int,input().split())
cat = X-A
if cat >= 0 and cat <= B :
    print('YES')
else:
    print('NO')