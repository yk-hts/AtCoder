N = int(input())
K = int(input())
sum = 1
for i in range(N):
    if sum*2 <= sum+K:
        sum *= 2
    else:
        sum += K
print(sum)