s = list(input())
n = int(input())

ans = s[int((n-1)/5)]+s[(n-1)%5]
print(ans)