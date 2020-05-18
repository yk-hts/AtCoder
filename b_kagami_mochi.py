n = int(input())
d = []
count = 1
for i in range(n):
    d.append(int(input()))

d.sort(reverse=True)

for i in range(1,len(d)):
    if d[i]<d[i-1]:
        count += 1

print(count)
