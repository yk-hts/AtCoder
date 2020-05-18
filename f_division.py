n = int(input())
a = n
cnt = 0

for k in range(2,a+1,1):
    n = a
    while n >= 1:
        if n%k==0:
            n /= k
        else:
            n -= k
        
        if n == 1:
            cnt+=1
        
print(cnt)