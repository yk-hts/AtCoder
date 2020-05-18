S = input()
C = ['A','B','C','D','E','F']
count = [0,0,0,0,0,0]

for i in range(len(S)):
    if S[i] in C:
        count[C.index(S[i])] += 1
result = ' '.join(map(str,count))
print(result)
