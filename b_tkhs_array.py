s = list(input())

count = 0
array = [s[0],1]
j = 1
a = ""
for i in range(1,len(s)):
    if s[i] == s[i-1]:
        array[j] += 1
    else:
        array.append(s[i])
        array.append(int(1))
        j += 2

print("".join([str(n) for n in array]))
