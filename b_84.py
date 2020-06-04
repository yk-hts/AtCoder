A,B = map(int,input().split())
S = list(input())
flag = True
num = ['0','1','2','3','4','5','6','7','8','9']

for i in range(A+B+1):
    if i != A:
        if S[i] not in num:
            flag = False
            break
    else:
        if S[i] != '-':
            flag = False
            break

if flag:
    print('Yes')
else:
    print('No')

          