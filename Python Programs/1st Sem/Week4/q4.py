date=input('Enter a date in the dd/mm/yyyy format\n')
dd,mm,yy=date.split('/')
dd=int(dd)
mm=int(mm)
yy=int(yy)
m30=[4,6,9,11]
m31=[1,3,5,7,8,10,12]
leap=False
valid=None
if ((yy%4==0)and(yy%100!=0)) or (yy%400==0):
    leap=True
if (mm<0 or mm>12) or dd<1 or (mm==2 and dd>29):
    valid=False
else:
    if (mm==2 and dd==29) and leap:
        dd=1
        mm+=1
        valid=True
    else:
        if (mm==2 and dd>28) and (not leap):
            valid=False
        elif (mm==2 and dd==28) and (not leap):
            dd=1
            mm+=1
            valid=True
if mm==12 and dd==31:
    dd=1
    mm=1
    yy+=1
    valid=True
elif ((mm in m30) and dd==30) or ((mm in m31) and dd==31):
    dd=1
    mm+=1
    valid=True
elif ((mm in m30) and dd>30) or ((mm in m31) and dd>31):
    valid=False
else:
    dd+=1
    valid=True
if valid:
    print('The date is valid and the next date is',dd,'/',mm,'/',yy)
else:
    print('Invalid date')
