N = int(input())
A = list(map(int,input().split()))
num = [[a,i] for a,i in enumerate(A,1)]

num.sort(key=lambda x:x[1],reverse=True)

for i in range(N):
    print(num[i][0])
    