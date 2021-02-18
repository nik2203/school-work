import pickle,os
from datetime import date

#functions

def issue(n,name):
    not_issued='False'
    today=date.today()
    d=today.strftime('%m-%d-%y')
    for i in range(0,len(n)):
        if n[i][1]==name and len(n[i])==2:
            n[i].append(d)
            not_issued='true'
        else:
            continue
    if not_issued=='False':
        print('The book is already issued')
    if not_issued=='true':
        print('The book has been issued')
        fh2=open('temp.dat','wb')
        pickle.dump(n,fh2)
        fh2.close()
        fh.close()
        os.remove('book.dat')
        os.rename('temp.dat','book.dat')

def return_b(n,name):
    issued='true'
    for i in range(0,len(n)):
        if n[i][1]==name and len(n[i])==3:
            n[i].remove(n[i][2])
            issued='false'
        else:
            continue
    if issued=='false':
        print('The book has been returned')
        fh2=open('temp.dat','wb')
        pickle.dump(n,fh2)
        fh2.close()
        fh.close()
        os.remove('book.dat')
        os.rename('temp.dat','book.dat')

#dictionaries
d1={1001:'In Search Of Lost Time',1002:'War and Peace',1003:'Don Quixote',1004:'The Great Gatsby',1005:'Lolita',1006:'One Hundred Years of Solitude'}
d2={1003:'23-03-2020',1002:'04-04-2020',1006:'01-05-2020'}

#A
l=[]
templ=[]
keys=list(d1.keys())
for i in range(len(keys)):
    templ.append(keys[i])
    templ.append(d1[keys[i]])
    if keys[i] in d2:
        templ.append(d2[keys[i]])
    l.append(templ)
    templ=[]
try:
    with open('book.dat','rb') as fh:
        a=pickle.load(fh)
except:
    with open('book.dat','wb') as fh:
        pickle.dump(l,fh)

#B
fh=open('book.dat','rb')
while True:
    try:
        a=pickle.load(fh)
    except EOFError:
        break
n=list(a)
x=input('are you issuing or returning a book (i/r) ')
if x=='i' or x=='I':
    name=input('enter the name of the book you want to issue ')
    issue(n,name)

if x=='r' or x=='R':
    name=input('enter the name of the book you want to return ')
    return_b(n,name)
