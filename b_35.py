S = list(input())
T = int(input())

x = 0
y = 0
count = 0
for i in range(len(S)):
    if S[i] == 'L':
        x -= 1
    elif S[i] == 'R':
        x += 1
    elif S[i] == 'U':
        y += 1
    elif S[i] == 'D':
        y -= 1
    else:
        count += 1

if T == 1:
    print(abs(x)+abs(y)+count)
else:
    n = abs(x)+abs(y)-count
    if n >= 0:
        print(abs(x)+abs(y)-count)
    else:
        if n%2==0:
            print(0)
        else:
            print(1)


# def calc_max(x,y):
#     ans = [[x,y]] * 4
#     ans[0][0] -= 1
#     ans[1][0] += 1
#     ans[2][1] -= 1
#     ans[3][1] += 1

#     for i in range()


