sum = 1
n = int(input())

for i in range(1,n+1):
    sum *= i

a = 10**9+7
print(sum%a)
