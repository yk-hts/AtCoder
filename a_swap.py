x = list(map(int,input().split()))
copy = x[0]
x[0] = x[1]
x[1] = copy

copy = x[0]
x[0] = x[2]
x[2] = copy

print(" ".join([str(i) for i in x]))
