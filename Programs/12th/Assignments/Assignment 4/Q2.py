def filedetails(fh):
    contents=fh.readlines()
    fh.seek(0)
    con=fh.read()
    w=con.split(' ')
    words=len(w)
    digits=0
    lines=len(contents)
    for i in range(len(w)):
        for j in w[i]:
            if j in '1234567890':
                digits+=1
    print(filename+'\n'+str(digits)+' digits in the file\n'+str(lines)+' lines in the file\n'+str(words)+' words in the file')
    fh.seek(0)


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
        
