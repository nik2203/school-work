from datetime import datetime

def time(t1,t2,x):
    form='%H:%M:%S'
    a=datetime.strptime(t1,form)
    b= datetime.strptime(t2, form)
    if x =='1' :
        td = a -b
    if x =='2':
        td = a-b
    if x=='3':
        td=a-b
    return td

t1=input('enter current time in hh:mm:ss format ')
x=input('enter which city you want:\n'
        '1. new york\n'
        '2. sydney\n'
        '3. johannesburg\n')
if x=='1':
    t2='09:30:00'
    print(time(t1,t2,x))
elif x=='2':
    t2='05:30:00'
    print(time(t1,t2,x))
elif x==3:
    t2='03:30:00'
    print(time(t1,t2,x))
''' I get the result for New York, it gives me an error for Sydney
and gives me nothing for Johannesburg '''
