x = int(input())
value = 100
count = 0

while value < x:
    value *= 1.01
    value = int(value)
    count += 1

print(count)