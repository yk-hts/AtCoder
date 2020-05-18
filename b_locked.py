a = int(input())
b = int(input())

if max(a,b)-min(a,b) >= 5:
    print(10-max(a,b)+min(a,b))
else:
    print(abs(a-b))