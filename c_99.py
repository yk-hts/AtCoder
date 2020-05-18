n = int(input())

ans = 2025-n

for i in range(1,9+1):
    if ans%i != 0:
        continue
    for j in range(1,9+1):
        if i*j == ans:
            print(str(i)+' x '+str(j))
            break