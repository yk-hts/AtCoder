import itertools
import collections
N = int(input())

num=[0]*5
for i in range(N):
    s=input()
    if s[0]=='M':
        num[0]+=1
    elif s[0]=='A':
        num[1]+=1
    elif s[0]=='R':
        num[2]+=1
    elif s[0]=='C':
        num[3]+=1
    elif s[0]=='H':
        num[4]+=1


ans = 0
for comb in itertools.combinations(num,3):
    ans+=comb[0]*comb[1]*comb[2]
print(ans)

# c = collections.Counter(array)
# n = len(array)
# ans = n*(n-1)*(n-2)//(3*2)

# for i in c:
#     if c[i] == 2:
#         ans -= n-c[i]
#     elif c[i] >= 3:
#         value = (c[i]*c[i]-1)//2-1
#         ans -= value

# print(ans)
    
