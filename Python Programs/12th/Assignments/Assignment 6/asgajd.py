import random

def check_speed(speed):
    global off
    global val
    if speed<70 and speed>0:
        return speed
    global dem
    if speed>70:
        off=1
        for i in range(70,speed+5,5):
            dem+=1
        if dem<12:
            off=1
        elif dem>=12:
            off=2
    elif speed<=0:
        val=1

dem=0
off=0
val=0
lic_no=''
for i in range(5):
    lic_no=lic_no+str(random.randint(0,9))
x=int(input('enter driver speed '))

res=check_speed(x)

if val==0:
    if off==0:
        print('License Number:'+lic_no+'\n'
              'Demerit Points:',dem,'\n'
              'Status: OK')
    if off==1:
        print('License Number:'+lic_no+'\n'
              'Demerit Points:',dem,'\n'
              'Status: Warning')
    if off==2:
        print('License Number:'+lic_no+'\n'
          'Demerit Points:',dem,'\n'
          'Status: License Suspended')
else:
    print('Invalid Data')
