import datetime as dt

#a

a=lambda x,y:x*y
x=int(input('Enter a number\n'))
y=int(input('Enter a number\n'))
print(a(x,y))

#b
sw=lambda x,y:True if x.startswith(y) else False
x=input('Enter the string\n')
y=input('Enter the starting letter to check\n')
print(sw(x,y))

#c
now=dt.datetime.now()
print('The system time is',now)
year=lambda x:x.year
month=lambda x:x.month
day=lambda x:x.day
t=lambda x:x.time()

print('The year is',year(now),'and the month is',month(now),'and the day is',day(now),'and the time is',t(now))

#d
d=[{'make':'Nokia','model':216,'colour':'black'},{'make':'Nokia','model':215,'colour':'red'},{'make':'Samsung','model':310,'colour':'blue'}]
x=input('Do you want to sort by:\n1. Make\n2. Model\n3.Colour\n')
if x=='1' or x=='Make' or x=='make':
    ma_s=sorted(d, key= lambda i:i['make'])
    print(ma_s)
if x=='2' or x=='Model' or x=='model':
    m_s=sorted(d , key = lambda i: i['model'])
    print(m_s)
if x=='3' or x=='Colour' or x=='colour':
    c_s=sorted(d, key= lambda i:i['colour'])
    print(c_s)