N,M,X = map(int,input().split())
A = list(map(int,input().split()))

cost =[0]*(N+1)

for i in A:
    cost[i] = 1

print(min(sum(cost[0:X]),sum(cost[X+1:])))
