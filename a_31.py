a,d = map(int,input().split())
attack = (a+1)*d
defense = a*(d+1)
if attack >= defense:
    print(attack)
else:
    print(defense)