a,b,c,k = map(int,input().split())
s,t = map(int,input().split())

if k <= s+t:
    print(a*s+b*t-c*(s+t))
else:
    print(a*s+b*t)