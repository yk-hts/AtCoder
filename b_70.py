A,B,C,D = map(int,input().split())

s = min(B,D)-max(A,C)

if s <= 0:
    s = 0

print(s)