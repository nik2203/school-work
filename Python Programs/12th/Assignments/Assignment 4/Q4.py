import os
fh=open('test.py','r')
fh1=open('test1.py','w')
l=fh.readlines()
for i in l:
    if i[0]=='#':
        l.remove(i)
fh1.writelines(l)
fh.close()
fh1.close()
os.remove('test.py')
os.rename('test1.py','test.py')
