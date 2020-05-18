A,B,C = map(int,input().split())

sum = C
ans = 'NO'
cnt = 0

while cnt < A:
    sum += B
    if sum % A == 0:
        print('YES')
        exit()
    cnt += 1
print('NO')

         

