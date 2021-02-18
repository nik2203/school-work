def writeae(filename):
    fh=open(filename,'r')
    l=fh.readlines()
    for i in l:
        if i[0] in 'AaeE':
            print(i)

x=input('enter filename w extension ')
writeae(x)
