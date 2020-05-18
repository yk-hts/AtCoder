n = int(input())
a = list(map(int,input().split()))

sum = 0

for i in range(n):
    answer = []
    for j in range(a[i]):
        if (j+1)%6 == 1 or (j+1)%6 == 3:
            answer.append('〇')
        else:
            answer.append('✕')
    
    for j in range(a[i]-1,-1,-1):
        if answer[j] == '〇':
            sum +=(a[i]-j-1)
            break
print(sum)
