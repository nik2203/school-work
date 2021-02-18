import csv


def write_csv(l):
    fh=open('students.csv','w')
    writer=csv.writer(fh)
    for i in l:
        writer.writerow(i)
    fh.close()

def find_student(n):
    fh=open('students.csv','r')
    reader=csv.reader(fh,delimiter=',')
    l=[]
    for row in reader:
        if row!=[]:
            l.append(row)
    if int(n)-1>len(l):
        print('This student does not exist')
    else:
        print(l[int(n)-1])

def  find_d():
    fh=open('students.csv','r')
    reader=csv.reader(fh,delimiter=',')
    l=[]
    l1=[]
    for row in reader:
        l.append(row)
    for i in l:
        if i==[]:
            l.remove(i)
        else:
            pass
    for i in l:
        if i[0][0][0]=='d':
           l1.append(i)
    print(l1)

def find_cricket():
    fh=open('students.csv','r')
    reader=csv.reader(fh,delimiter=',')
    l=[]
    l1=[]
    for row in reader:
        l.append(row)
    for i in l:
        if i==[]:
            l.remove(i)
        else:
            pass
    for i in l:
        if i[1]=='cricket':
           l1.append(i)
    print(l1)

    
students=[['amogh','football'],['aditya','cricket'],['suma','basketball'],['dev','basketball'],['sourabh','football']]
write_csv(students)
x=input('do you want to:\n'
        '1. Find nth student\n'
        '2. Display names of students with name beginning with D\n'
        '3. Display names of students who play cricket\n')
if x=='1':
    n=input('enter student no. ')
    find_student(n)
if x=='2':
    find_d()
if x=='3':
    find_cricket()
