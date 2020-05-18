a,b,c = map(int,input().split())
plus = a+b
minus = a-b

if plus == c and minus == c:
    print('?')
elif plus == c:
    print('+')
elif minus == c:
    print('-')
else:
    print('!')