num = ["1","2","3","4","5","6"]
n = int(input())%30
for i in range(n):
    num[i%5],num[i%5+1] = num[i%5+1],num[i%5]

print("".join(num))
    