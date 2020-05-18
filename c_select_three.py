import math
import itertools
n = list(map(int,input().split()))
m = list(itertools.combinations(n,3))

s = []
for i in range(len(m)):
    s.append(sum(m[i]))
    
sum_list = list(set(s))
sum_list.sort()
print(sum_list[-3])