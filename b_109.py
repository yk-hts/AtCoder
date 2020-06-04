N = int(input())
W = [input() for _ in range(N)]
flag = True

for i in range(1,N):
    if W[i-1][-1] != W[i][0]:
        flag = False

if len(W) ==  len(set(W)) and flag:
    print('Yes')
else:
    print('No')