s = list(input())
t = list(input())

s.sort()
t.sort(reverse=True)

if ord(s[0]) < ord(t[0]):
    print('Yes')
elif ord(s[0]) == ord(t[0]):
    for i in range(min(len(s),len(t))):
        if ord(s[i]) > ord(t[i]):
            print('No')
            exit()
    if len(s) < len(t):
        print('Yes')
    else:
        print('No')
else:
    print('No')