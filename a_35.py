W,H = map(int,input().split())

for i in range(min(W,H),0,-1):
    if W%i == 0 and H%i == 0:
        print(str(int(W/i))+':'+str(int(H/i)))
        exit()
    