n = int(input())
ng = [int(input()) for i in range(3)]
if n in ng:
    print('NO')
    exit()

for i in range(100):
    n -= 3
    if n in ng or n < 0:
        n += 3
        n -= 2
        if n in ng or n < 0:
            n += 2
            n -= 1
            if n in ng:
                print('NO')
                exit()

    if n == 0:
        print('YES')
        exit()
    elif n < 0:
        print('NO')
        exit()
print('NO')