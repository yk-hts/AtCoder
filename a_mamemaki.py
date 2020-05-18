a = int(input())
b = int(input())
c = int(input())

array = [a,b,c]
array.sort(reverse = True)
print(array.index(a)+1)
print(array.index(b)+1)
print(array.index(c)+1)
