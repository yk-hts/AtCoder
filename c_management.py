n = int(input())
a = list(map(int,input().split()))
x = [0] * n

for i in range(len(a)):
    x[a[i]-1] += 1

print(x[i] for i in range(len(x)))
    
