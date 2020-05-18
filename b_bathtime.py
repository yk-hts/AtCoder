def answer(time):
    if time < 10:
        print(str('0'+time+':',end=""))
    else:
        print(str(time+':',end=""))

n = int(input())

hour = int(n/3600)
n -= hour*3600
if hour < 10:
    print('0'+str(hour)+':',end="")
else:
    print(str(hour)+':',end="")
minute = int(n/60)
n -= minute*60
if minute < 10:
    print('0'+str(minute)+':',end="")
else:
    print(str(minute)+':',end="")
if n < 10:
    print('0'+str(n))
else:
    print(str(n))
