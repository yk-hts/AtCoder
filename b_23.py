n = int(input())
s = list(input())
ans = ['b']
array_plus = ['c','a','b']
array_minus = ['a','c','b']
for i in range(int(n/2)):
    ans.append(array_plus[i%3])
    ans.insert(0,array_minus[i%3])

if ans == s:
    print(int(n/2))
else:
    print(-1)


 

    
    


