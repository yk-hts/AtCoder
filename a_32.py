a = int(input())
b = int(input())
n = int(input())

judge = True

while judge:
    if n%a == 0 and n%b == 0:
        judge = False
    else:
        n += 1
print(n)