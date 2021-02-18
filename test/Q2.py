import os

def word_count(fh):
    l=fh.read()
    l=l.split(' ')
    word_count=0
    for i in l:
        if i=='cbse':
            word_count+=1
    print(word_count)

def update(fh)
    l=fh.read()
    l=l.split(' ')
    for i in l:
        if i=='cbse':
            i='CBSE'
    fh1=open('temp.txt','w')
    fh1.write(' '.join(l))
    fh.close()
    fh1.close()
    os.remove('cbse.txt')
    os.rename('temp.txt','cbse.txt')
    
x=input('enter file name ')
fh=open(x,'r')
word_count(fh)
fh.close()
