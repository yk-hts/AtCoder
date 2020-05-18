S = list(input().split('+'))
count = 0
for i in range(len(S)):
    if '0' not in S[i]:
        count += 1
print(count)



# for i in range(len(S)):
#     if i%2 != 0:
#         if S[i]=='+' and S[i-1] != '0':
#             count += 1
    