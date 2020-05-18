x = int(input())
cnt = 0
i = 0
while cnt <= x:
    i += 1
    if i < 10:
        cnt+=1
    elif i < 100:
        if abs(int(i/10)-(i-int(i/10)*10))<= 1:
            cnt+=1
    elif i < 1000:
        if abs(int(i/100)-(i-int(i/100)*100))<= 1 and abs(int(i/10)-(i-int(i/10)*10))<= 1:
            cnt+=1
    elif i < 10000:
        if abs(int(i/10)-(i-int(i/10)*10))<= 1 and abs(int(i/100)-(i-int(i/100)*100))<= 1 and abs(int(i/1000)-(i-int(i/1000)*1000))<= 1:
            cnt+=1
    elif i < 100000:
        if abs(int(i/10)-(i-int(i/10)*10))<= 1 and abs(int(i/100)-(i-int(i/100)*100))<= 1 and abs(int(i/1000)-(i-int(i/1000)*1000))<= 1 and abs(int(i/100000)-(i-int(i/100000)*100000))<= 1:
            cnt += 1

        
        
    if cnt == x:
        print(i)
        break

    
