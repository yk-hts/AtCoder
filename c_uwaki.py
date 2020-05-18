import math
sx,sy,gx,gy,t,v = map(int,input().split())
n = int(input())
x_y = []
sum = 0
for i in range(n):
    x,y = map(int,input().split())
    x_y.append([x,y])

for i in range(len(x_y)):
    sum = 0
    sum += math.sqrt(((x_y[i][0]-sx)**2+(x_y[i][1]-sy)**2))+math.sqrt(((gx-x_y[i][0])**2+(gy-x_y[i][1])**2))
    if sum <= t*v:
        print('YES')
        exit()
print('NO')
