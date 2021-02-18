x=eval(input('Enter 10 numbers '))
mean=0
sta=[]
stand=0
if len(x)>10:
    print('invalid')
if len(x)<10:
    print('invalid')
else:
    for i in range(len(x)):
        mean+=x[i]
    mean=mean/10
    for i in range(len(x)):
        sta.append(x[i]-mean)
    for i in range(len(sta)):
        stand+=(sta[i])**2
    stand=int((stand/10)**(1/2))
    print(stand)
