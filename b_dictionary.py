s = list(input())

if len(s) == 1:
    if s[0] == 'a':
        print(-1)
    else:
        print(chr(ord(s[0])-1))
else:
    s.remove(s[len(s)-1])
    print(''.join(s))