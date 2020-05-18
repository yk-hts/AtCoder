n = int(input())
min = n-1
for i in range(1,int((n+1)/2)):
    a = int(n/i)
    b = n-a*i
    comp = abs(i-a)+b
    if comp < min:
        min = comp
print(min)