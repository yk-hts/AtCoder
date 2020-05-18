n,a,b = map(int,input().split())
s = []
d = []
distance = 0
judge = 0

for i in range(n):
    x,y = map(str,input().split())
    s.append(x)
    d.append(int(y))

for i in range(n):
    if d[i] < a:
        distance = a
    elif d[i] > b:
        distance = b
    else:
        distance = d[i]
    
    if s[i] == 'East':
        judge += distance
    else:
        judge -=distance

if judge < 0:
    print('West ',end="")
elif judge > 0:
    print('East ' ,end="")

print(abs(judge))

