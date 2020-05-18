import itertools

s = input()
k = int(input())

array = []
for i in range(len(s)-(k-1)):
    array.append(s[i:i+k])

print(len(set(array)))