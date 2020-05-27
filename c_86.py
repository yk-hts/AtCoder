n = int(input())

now = [0,0,0]
for i in range(n):
    s = list(map(int,input().split()))
    time = s[0] - now[0]
    dis = abs(s[1] - now[1]) + abs(s[2] - now[2])
    if time < dis or (time-dis)%2 == 1:
        print("No")
        exit()
    now = s

print("Yes")
