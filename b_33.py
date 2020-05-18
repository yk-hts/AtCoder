n = int(input())
s = []
p = []

for i in range(n):
    a,b = map(str,input().split())
    s.append(a)
    p.append(int(b))

sum_p = sum(p)

for i in range(n):
    if p[i] > int(sum_p/2):
        print(s[i])
        exit()
print('atcoder')