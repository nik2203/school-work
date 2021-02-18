fh=open('dance in the rain.txt','r')
fh1=open('repeated lines.txt','a')
l=fh.readlines()
l2=[]
for i in range(len(l)):
    if i==1 or i==3:
        l2.append(l[i])
    elif i>4 and l[i] not in l2 and l[i]!='\n':
        l2.append(l[i])
fh1.writelines(l2)
fh.close()
fh1.close()
