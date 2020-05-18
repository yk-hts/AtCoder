A,B = map(int,input().split())
array = [2,3,4,5,6,7,8,9,10,11,12,13,1]
if array.index(A) > array.index(B):
    print('Alice')
elif array.index(A) == array.index(B):
    print('Draw')
else:
    print('Bob')