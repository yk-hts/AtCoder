a = int(input())
b = int(input())

if a <= b:
    print(b-a)
else:
    print(b-(a%b))