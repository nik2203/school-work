cc={'u.k':'london','vietnam':'ho chi minh', 'japan':'tokyo','russia':'moscow','france':'paris','india':'new delhi','sri lanka':'colombo'}
x=int(input('do you want to find:\n1. a city\n2. a country '))
if x==1:
    c=input('enter a country ')
    if c in cc:
        print(cc[c])
    else:
        print('not listed')
elif x==2:
    c=input('enter a city ')
    if c in cc.values():
        print(list(cc.keys())[(list(cc.values()).index(c))])
    else:
        print('not listed')
