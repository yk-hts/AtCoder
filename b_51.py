K,S = map(int,input().split())
array = [i for i in range(K+1)]
cnt = 0

for i in array:
    for j in array:
        h = S-(i+j)
        if h >= 0 and h <= K:
            cnt += 1
print(cnt)
