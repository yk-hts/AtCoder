s = input()
n = int(input())
for i in range(n):
    b,e = map(int,input().split())
    copy = s[b-1:e]
    s = s[0:b-1]+copy[::-1]+s[e:]
print(s)


