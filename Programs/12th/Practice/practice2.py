'''
def lineno(x):
    ctr=1
    for i in x.readlines():
        print(ctr,i,end='')
        ctr+=1

#opening the file
doc1=open('doc1.txt')
lineno(doc1)
doc1.close()


def append(x,y):
    ctr=0
    for i in x.readlines():
        ctr+=1
        if ctr%2==0:
            y.write(i)


#opening the file
doc1=open('doc1.txt','r')
doc2=open('doc2.txt','a')
append(doc1,doc2)
doc1.close()
doc2.close()
'''
def remove_comment(x):
    l=x.readlines()
    print('The file without the comments is:')
    for i in l:
        if i[0]=='#':
            l.remove(i)
    for j in l:
        print(j,end='')

#opening
doc1=open('doc1.txt')
remove_comment(doc1)
doc1.close()
