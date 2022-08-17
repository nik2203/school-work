n=int(input('Enter no. of students '))
d={}
for i in range(n):
    key=input('Enter student no. ')
    if key in d:
        print('invalid')
    else:
        d[key]={}
        d[key]['name']=input('enter student name ')
        d[key]['age']=input('enter your age ')
        d[key]['roll number']=input('enter roll.no ')
        d[key]['p_marks']=int(input('enter physics marks '))
        d[key]['c_marks']=int(input('enter chemistry marks '))
        d[key]['m_marks']=int(input('enter maths marks '))
ctr=int(input('choose a program:\n1.highest physics marks\n2.lowest marks in chemistry\
\n3.percentage and fail/pass\n4.name for roll no. '))
if ctr==1:
    mm=0
    for i in d:
        if d[i]['p_marks']>mm:
            mm=d[i]['p_marks']
        else:
            continue
    for i in d:
        if d[i]['p_marks']==mm:
            print(d[i]['name'],mm)
if ctr==2:
    mim=int(input('enter max marks '))
    for i in d:
        if d[i]['c_marks']<mim:
            mim=d[i]['c_marks']
    for i in d:
        if d[i]['c_marks']==mim:
            print(d[i]['name'],mim)
if ctr==3:
    name=input('enter student name ')
    mm=int(input('enter max marks '))
    pp=int(input('enter pass percentage '))
    for i in d:
        count=0
        if d[i]['name']==name:
            count+=1
            perc=(((d[i]['p_marks']+d[i]['c_marks']+d[i]['m_marks'])/3)/mm)*100
            if perc>pp:
                print('pass')
            else:
                print('fail')
        else:
            continue
    if count>0:
        print('invalid')
if ctr==4:
    roll=input('enter roll no. ')
    for i in d:
        if d[i]['roll number']==roll:
            print(d[i]['name'])
