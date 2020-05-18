import itertools
n = int(input())
l = 'abc'
a = itertools.product('abc',repeat = n)
for i in a:
    print(''.join(i))