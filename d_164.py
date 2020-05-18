s = input()
n = len(s)
count = 0
i = 0
while i <= n-3:
    for j in range(i+4,n+1):
        if int(s[i:j])%2019 == 0:
            count += 1
            i = j-1
            break
    i += 1
print(count)

