'''
def alphnum(x):
    alp=0
    num=0
    for i in x.read():
        if i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            alp+=1
        elif i in '0123456789':
            num+=1
    print('Alphabets:',alp,'Numbers:',num)

#Opening doc1
doc1=open('doc1.txt')
alphnum(doc1)
doc1.close()
'''
def words(x):
    wc=0
    s=x.read().split()
    for i in s:
        wc+=1
    print('There are',wc,'words in the file')

#opening doc1
doc1=open('doc1.txt')
words(doc1)
docs1.close()
