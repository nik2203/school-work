'''
Q1
x=input('Do you want to begin (y/n)\n')
while x=='y' or x=='Y':
    l=eval(input('Enter a list\n')) #takes in list to reverse
    if type(l)==list:
        lp=0 #initialises the left counter
        rp=len(l)-1 #initialises the right counter
        while lp<rp: #continues till left counter equals right counter
            l[lp],l[rp]=l[rp],l[lp] #swaps elements
            lp+=1 #increases left counter
            rp-=1 #decreases right counter
        print('The reversed list is',l)
    else:
        print('You have not entered a list. Try again')
    x=input('Do you want to continue (y/n)\n')

#Q2
x=input('Do you want to begin (y/n)\n')
while x=='y' or x=='Y':
    s=input('Enter a sentence\n') #takes in sentence to reverse and capitalisation
    l=s.split(' ')
    l=l[::-1]
    for i in l:
        if len(i)>2:
            print(i[0].upper()+i[1:len(i)-1]+i[-1].upper(),end=' ')
        else:
            print(i.upper(),end=' ')
    x=input('\nDo you want to continue (y/n)\n')

#Q3
x=input('Do you want to begin (y/n)\n')
while x=='y' or x=='Y':
    d1=eval(input('Enter a dictionary\n'))
    d2=eval(input('Enter another dictionary\n'))
    d3=d1
    for i in d2:
        if i in d3:
            d3[i]=d3[i]+d2[i]
        else:
            d3[i]=d2[i]
    print('The resulting dictionary is',d3)
    x=input('Do you want to continue (y/n)\n')


#Q4
x=input('Do you want to begin (y/n)\n')
while x=='y' or x=='Y':
    mat=eval(input('Enter a 3xN matrix\n')) #takes in a matrix with 3 columns and N rows
    for i in mat: #Going through rows
        for j in range(1,3): #Going through columns of row
            key=i[j]
            k=j-1
            #Moves elements greater than the key to right
            while k>=0 and key<i[k]:
                i[k+1]=i[k]
                k-=1
            i[k+1]=key
    n=len(mat)
    for i in range(n-1):#Goes through matrix elements
        for j in range(n-i-1): #Ignores last, sorted i no. of elements
            if mat[j]>mat[j+1]: #If preceding element greater than following
                mat[j],mat[j+1]=mat[j+1],mat[j] #Swaps them
    print(mat)
    x=input('Do you want to continue (y/n)\n')

#Q5

def circle_collide(x1,y1,r1,x2,y2,r2):
    rsum=r1+r2 #gives the sum of radii
    dist=int((((x1-x2)**2)+((y1-y2)**2))**0.5) #calculates the distance between the centres of the circles
    if dist<=rsum: #if the sum of radii is greater than or equal to the distance between the circles
        return True #colliding
    else:
        return False #not colliding

x=input('Do you want to begin (y/n)\n')
while x=='y' or x=='Y':
    x1=int(input('Enter the x co-ordinate of circle 1\n'))
    y1=int(input('Enter the y co-ordinate of circle 1\n'))
    r1=int(input('Enter the radius of circle 1\n'))
    x2=int(input('Enter the x co-ordinate of circle 2\n'))
    y2=int(input('Enter the y co-ordinate of circle 2\n'))
    r2=int(input('Enter the radius of circle 2\n'))
    coll=circle_collide(x1,y1,r1,x2,y2,r2)
    if coll:
        print('The circles are colliding')
    else:
        print('The circles are not colliding')
    x=input('Do you want to continue (y/n)\n')


#Q6
def find_a(v1=1,v2=1,t=1):
    acc=int((v2-v1)/t)
    return acc

def find_force(m=1,v1=1,v2=1,t=1):
    force=m*find_a(v1,v2,t)
    return force

x=input('Do you want to begin (y/n)\n')
while x=='y' or x=='Y':
    x1=int(input('Do you want to find:\n'
                 '1. Force\n'
                 '2. Acceleration\n'))
    vel1=int(input('Enter initial velocity \n'))
    vel2=int(input('Enter velocity at time t\n'))
    tim=int(input('Enter time in seconds\n'))
    if x1==1:
        mass=int(input('Enter mass of the object\n'))
        print('The force is',find_force(m=mass,v1=vel1,v2=vel2,t=tim),'N')
    if x1==2:
        print('The acceleration is',find_a(v1=vel1,v2=vel2,t=tim),'m/s^2')
    x=input('Do you want to continue (y/n)\n')


#Q7
def sum_all(l):
    su=0
    for i in l:
        if type(i)==int:
            su+=i
        else:
            return 'Incompatible values. Try again'
    return su

def prod_all(*l):
    prod=1
    for i in l:
        if type(i)==int:
            prod*=i
        else:
            return 'Incompatible values. Try again'
    return prod

x=input('Do you want to begin (y/n)\n')
while x=='y' or x=='Y':
    x1=int(input('Do you want to find:\n'
                 '1. Sum\n'
                 '2. Product\n'))
    if x1==1:
        l=eval(input('How many numbers
    if x1==2:
        l=eval(input('Enter a list of numbers to multiply\n'))
        print('The product is',prod_all(l))
    x=input('Do you want to continue (y/n)\n')


#Q8
cap='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
vow='aeiou'
spec='!"\'#~-+=_$%&*()@?/][}{;:.,><'

x=input('Do you want to begin (y/n)\n')
while x=='y' or x=='Y':
    ins=input('Enter a string \n')
    capc=0
    vowc=0
    specc=0
    numc=0
    for i in ins:
        if i in cap:
            capc+=1
            if i.lower() in vow:
                vowc+=1
        elif i in vow:
            vowc+=1
        elif i in spec:
            specc+=1
        elif i.isnumeric():
            numc+=1
    print('There are\n',
        capc,'Capital letters\n',
        vowc,'Vowels\n',
        specc,'Special Characters\n',
        numc,'Numbers\n In the string '+ins)
    x=input('Do you want to continue (y/n)\n')

#Q9

from modules import validate
x=input('Do you want to begin (y/n)\n')
while x=='y' or x=='Y':
    prog=int(input('Do you want to:\n 1. Generate an OTP\n 2. Generate a CAPTCHA\n 3. Validate an email\n'))
    if prog==1:
        print('Your OTP is '+validate.genotp())
    if prog==2:
        print('CAAPTCHA:'+validate.gencap())
    if prog==3:
        validate.valemail()
    x=input('Do you want to continue (y/n)\n')


#Q10
import urllib.request, re

x=input('Do you want to begin (y/n)\n')
while x=='y' or x=='Y':
    wl=input('Enter the URL of the website\n')
    with urllib.request.urlopen(wl) as resp:
        html=resp.read()
        text=html.decode('utf8')
        links=re.findall("href=[\"\'](.*?)[\"\']", text)
        print(links,end='\n')
    x=input('Do you want to continue (y/n)\n')


#Q11
import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
can=tk.Canvas(root,width=300,height=300)
can.pack()

def ex():
    warning=tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    while warning!='yes':
        warning=tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    else:
        root.destroy()
btn=tk.Button(root, text='Exit Application',command=ex,bg='brown',fg='white')
can.create_window(150, 150, window=btn)
root.mainloop()

#Q12
x=input('Do you want to begin (y/n)\n')
while x=='y' or x=='Y':
    from datetime import date

    date1=input('enter the current date in (yyyy/mm/dd) format ')
    date2=input('enter the date in the same format ')
    d1=tuple(date1.split('/'))
    d2=tuple(date2.split('/'))
    date1=date(int(d1[0]),int(d1[1]),int(d1[2]))
    date2=date(int(d2[0]),int(d2[1]),int(d2[2]))
    print((date2-date1).days,'days')
    x=input('Do you want to continue (y/n)\n')

#Q13
x=input('Do you want to begin (y/n)\n')
while x=='y' or x=='Y':
    fh1=open('Our Generation.txt','r')
    fh2=open('reversePoem.txt','w+')
    lines=fh1.readlines()
    lines.reverse()
    fh2.writelines(lines)
    fh1.close()
    fh2.seek(0)
    print(fh2.read())
    fh2.close()
    x=input('Do you want to continue (y/n)\n')


#Q14
def filedetails(fh):
    contents=fh.readlines()
    fh.seek(0)
    con=fh.read()
    w=con.split(' ')
    words=len(w)
    lines=len(contents)
    print(filename+'\n'+str(lines)+' lines in the file\n'+str(words)+' words in the file')
    fh.seek(0)

x=input('Do you want to begin (y/n)\n')
while x=='y' or x=='Y':
    filename=input('enter file name with extension ')
    fh=open(filename,'r')
    filedetails(fh)
    read=fh.readlines()
    for i in read:
        print(i)
        if i[-2:-6:-1]=='txt.':
            f=open(i[0:len(i)-1],'r')
            filedetails(f)
            f.close
    fh.close()
    x=input('Do you want to continue (y/n)\n')

#Q15

import pickle

x=input('Do you want to begin (y/n)\n')
while x=='y' or x=='Y':
    countries=[['Afghanistan','Kabul','34.28N','69.11E'],['Albania','Tirane','41.18N','19.49E'],['Algeria','Algiers','36.42N','03.08E'],['Iceland','Reykjavik','64.10N','21.57W'],['India','New Delhi','28.73N','77.13E'],['Indonesia','Jakarta','06.09S','106.49E']]

    fh=open('countries.dat','wb')
    for i in countries:
        pickle.dump(', '.join(i)+'\n',fh)
    fh.close()

    with open('countries.dat','rb') as fh:
        l=[]
        while True:
            try:
                a=pickle.load(fh)
                l.append(a)
            except EOFError:
                break

    count=input('enter country for country details\n')
    pres=0
    for i in l:
        if count in i:
            print(i)
            pres+=1
    if pres==0:
        print('The country is not on the list')
    x=input('Do you want to continue (y/n)\n')


#Q16

import pickle
import os

x=input('Do you want to begin (y/n)\n')
while x=='y' or x=='Y':
    col1={'WHITE':'#FFFFFFF','SILVER':'#C0C0C0','GRAY':'#808000',}
    col2={'BLACK':'#000000','RED':'#FF0000','MAROON':'#800000'}
    col3={'YELLOW':'#FFFF00','OLIVE':'#808000','LIME':'#00FF00'}
    l=[col1,col2,col3]


    fh=open('colours.bin','wb')
    for i in l:
        pickle.dump(i,fh)
    fh.close()

    #b
    fh=open('colours.bin','ab+')
    pickle.dump({'GREEN':'#008000'},fh)
    fh.seek(0)
    fh.close()

    #c
    fh1=open('colours.bin','rb')
    fh2=open('temp.bin','wb')
    while True:
        try:
            a=pickle.load(fh1)
            if 'GRAY' in a.keys():
                a['GRAY']='#808080'
                pickle.dump(a,fh2)
            else:
                pickle.dump(a,fh2)
        except EOFError:
            break
    fh1.close()
    fh2.close()
    os.remove('colours.bin')
    os.rename('temp.bin','colours.bin')
    x=input('Do you want to continue (y/n)\n')


#Q17
import csv

x=input('Do you want to begin (y/n)\n')
while x=='y' or x=='Y':
    year=input('enter year ')

    print('The Robert diNero movies from '+year+' are:\n')

    l=[]
    l1=[]

    with open('diNero.csv','r') as fh:
        data=csv.reader(fh)
        for i in data:
            l1.append(i)
        for i in range(len(l1)-1):
            l.append(l1[i][1])
            if l1[i][0]==year:
                print(l1[i][2])
        mini=min(l[1:])
        maxi=max(l[1:])
        lowest=[]
        highest=[]
        for i in l1:
            if i[1]==mini:
                lowest.append(i)
            if i[1]==maxi and i[1]!='   Score':
                highest.append(i)
        print('His highest rated movie(s) is/are:\n',highest,sep='\n')
        print('His lowest rated movie(s) is/are\n',lowest,sep='\n')

    with open('diNero.csv','a') as fh:
        rows=[["2015","    60","Joy"],["2015","    26","Heist"],["2015","  61","The Intern"]]
        writer=csv.writer(fh)
        writer.writerows(rows)
    x=input('Do you want to continue (y/n)\n')


#Q19
from modules import listops
x=input('Do you want to begin (y/n)\n')
while x=='y' or x=='Y':
    ar=eval(input('Enter a list of 10 characters of the same data type\n'))
    sear=input('Enter the element to search for\n')
    if type(ar[0])==int:
        sear=int(sear)
    if type(ar[0])==list:
        sear=[sear]
    if type(ar[0])==tuple:
        sear=(sear)
    prog=int(input('Do you want  to:\n 1.Perform binary search for an element\n 2. Perform linear search for an element\n'))
    if prog==1:
        u=len(ar)
        listops.bin_sear(0,u,ar,sear)
    if prog==2:
        listops.ar_search(ar,sear)
    x=input('Do you want to continue (y/n)\n')

#Q20
def capit(ar):
    res=[]
    for i in ar:
        res.append(i.capitalize())
    return res

x=input('Do you want to begin (y/n)\n')
while x=='y' or x=='Y':
    ar=eval(input('enter an array of words '))
    print(capit(ar))
    x=input('Do you want to continue (y/n)\n')

#Q21
def upper(mat,n):
    for i in range(n): 
        for j in range(n):
            if (i>j):
                print(' ',end=' ')
            else: 
                print(mat[i][j],end=' ') 
        print()
def lower(mat,n):
    for i in range(0,n):
        for j in range(i+1):
            print(mat[i][j],end=' ')
        print()

x=input('Do you want to begin (y/n)\n')
while x=='y' or x=='Y':
    mat=eval(input('enter a n x n  matrix '))
    n=len(mat)
    x=int(input('do you want to see:\n'
                '1. the upper half\n'
                '2. the lower half\n'))
    if x==1:
        upper(mat,n)
    if x==2:
        lower(mat,n)
    
    x=input('Do you want to continue (y/n)\n')
'''
#Q22
x=input('Do you want to begin (y/n)\n')
while x=='y' or x=='Y':
    dim=int(input('Enter the dimensions of the matrix\n'))
    ar1=eval(input('Enter a matrix of the dimensions '+str(dim)+'\n'))
    ar2=eval(input('Enter a matrix of the dimensions '+str(dim)+'\n'))
    res=[]
    for i in range(dim):
        res.append([])
        for j in range(dim):
            res[i].append(0)
    for i in range(len(ar1)):  
        for j in range(len(ar2[0])): 
            for k in range(len(ar2)): 
                res[i][j] += ar1[i][k] * ar2[k][j] 
  
    for r in res: 
        print(r)
    x=input('Do you want to continue (y/n)\n')
#Q23
def push(arr,top,x):
    if top!=0:
        arr.append(x)
        top+=1
        return top
    else:
        arr.append(x)
        top=1
        return top


def pop(arr,top):
    if top==-1 or top==None:
        print('the array is empty')
    else:
        x=arr.pop()
        print(x)
        top-=1
        if top==-1:
            top=None
        return top
#q24
subp=int(input('What do you want to do:\n' #subp- sub program
                '1. Try popping on an empty stack\n'
                '2. Push 2 elements into a stack\n'
                '3. Pop an element from a stack\n'))
if subp==1:
    arr=eval(input('Enter an array\n'))
    pop(arr,-1)
if subp==2:
    arr=eval(input('Enter an array\n'))
    top=len(arr)-1
    for i in range(2):
        el=input('Enter element to push\n')
        push(arr,top,el)
        top+=1
    print(arr)
if subp==3:
    arr=eval(input('Enter an array\n'))
    top=len(arr)-1
    pop(arr,top)
    top-=1
    print(arr)

#q25
x=int(input('Enter a number\n'))
arr=[]
top=-1
while x>0:
    push(arr,top,x%2)
    x//=2
    top+=1
while top>-1:
    print(pop(arr,top)[0],end='')
    top-=1

#q26
def enq(arr,front,rear,x):
    if front==None or front==-1:
        arr[0:]=[x]
        front=rear=0
    else:
        arr.append(x)
        rear+=1
    return

def deq(arr,front,rear):
    if front==-1 or front==None:
        print('queue is empty')
    if front==rear:
        print(arr.pop(front))
        front=rear=None
    else:
        print(arr.pop(front))
    return
#q27