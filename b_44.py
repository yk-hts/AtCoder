w = list(input())
W = list(set(w))
cnt = [0]*len(W)

for i in w:
    cnt[W.index(i)] += 1

for i in cnt:
    if i%2!=0:
        print('No')
        exit()
print('Yes')
