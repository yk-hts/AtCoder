import itertools

n,k = map(int,input().split())
answer = []
i = 0
a = [10**6+i+1] * n
for j in range(k,len(a)+1):
    sum_list = list(itertools.combinations(a,j))
    for i in range(len(sum_list)):
        answer.append(sum(sum_list[i]))
print(len(set(answer)))

