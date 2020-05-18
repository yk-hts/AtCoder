S = [list(input()) for _ in range(3)]
member = ['a','b','c']
ans = ['A','B','C']
player = 0
cnt = 0

for i in range(len(S)):
    cnt += len(S[i])

for i in range(cnt):
    if len(S[player]) == 0:
        print(ans[player])
        exit()
    player = member.index(S[player].pop(0))

