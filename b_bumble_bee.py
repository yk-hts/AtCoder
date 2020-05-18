n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
print(len(a)-len(set(a)))