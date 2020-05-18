n = int(input())
b = [int(input()) for i in range(n-1)]
s = [[] for _ in range(n+1)]
for i in range(n,0,-1):
    if len(s[i]) == 0:
        s[i] = 1
    else:
        s[i] = max(s[i])+min(s[i])+1
    if i-2 >= 0:
        s[b[i-2]] += [s[i]]
    print(s)
print(s[i])


# for i in range(n):
#     if (i+1) not in b:
#         money[i] = 1
# ans_all = []
# for i in range(n):
#     if money[i] == 0:
#         ans = []
#         for j in range(len(b)):
#             if b[j] == i+1:
#                 ans.append(j+2)
#         ans_all.append(ans)

# for i in range(n-1,-1,-1):
#     if money[i] == 0:
#         if len(ans_all[i]) == 1:
#             money[i] = money[i+1]*2+1
#         else:
#             min = money[ans_all[i][0]-1]
#             max = money[ans_all[i][1]-1]
#             money[i] = min + max +1
#             for j in range(len(ans_all[i])):
#                 if money[ans_all[i][j]-1] < min:
#                     min = money[ans_all[i][j]-1]
#                     if money[ans_all[i][j]-1] > max:
#                         max = money[ans_all[i][j]-1]
#             money[i] = min+max+1

# print(money[0])