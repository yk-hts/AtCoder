s = list(input())

for i in range(len(s)):
    if s[i] >= 'a' and s[i] <= 'z':
        if i == 0:
            s[i] = chr(ord(s[i])-32)
    else:
        if i != 0:
            s[i] = chr(ord(s[i])+32)

print(''.join(s))

