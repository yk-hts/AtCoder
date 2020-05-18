N = int(input())
A = list(map(int,input().split()))

color = [0]*8
count = 0

for a in A:
    if a < 400:
        color[0] = 1
    elif a < 800:
        color[1] = 1
    elif a < 1200:
        color[2] = 1
    elif a < 1600:
        color[3] = 1
    elif a < 2000:
        color[4] = 1
    elif a < 2400:
        color[5] = 1
    elif a < 2800:
        color[6] = 1
    elif a < 3200:
        color[7] = 1
    else:
        count += 1
sum_color = sum(color)

if sum_color == 0:
    print(1,count)
else:
    print(sum_color,sum_color+count)