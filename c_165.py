import itertools
n,m,q = map(int,input().split())

A = [i for i in range(1,m+1)]
A_list = list(itertools.combinations_with_replacement(A,n))
max_sum = [0]*len(A_list)

for i in range(q):
    a,b,c,d = map(int,input().split())
    for j in range(len(A_list)):
        if A_list[j][b-1]-A_list[j][a-1] == c:
            max_sum[j] += d
print(max(max_sum))


//combinationは重複なしcombination_with_replaceは重複あり