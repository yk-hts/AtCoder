n = int(input())
s = [int(input()) for _ in range(n)]

s_set = list(set(s))
s_count = [0] * len(s_set)

for i in range(len(s_set)):
    for j in range(len(s)):
        if s_set[i] == s[j]:
            s_count[i]+=1
print(s_set[s_count.index(max(s_count))])



