def read_bytes(fh):
    l=fh.read()
    byte_count=0
    for i in l:
        if i !='\n':
            byte_count+=1
    return byte_count

def append_file(file1,file2):
    fh1=open(file1,'a')
    fh2=open(file2,'r')
    l=fh2.read()
    fh1.write(l)
    fh1.close()
    fh2.close()
    

#A
x=input('enter file name ')
fh=open(x,'r')
print('The number of bytes in '+x+' is',read_bytes(fh))

#B
x=input('enter file name ')
y=input('enter file name to be appended ')
append_file(x,y)
