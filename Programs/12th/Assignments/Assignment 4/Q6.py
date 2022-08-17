def invite(name):
    fh1=open('format.txt','r')
    fh2=open('invitations.txt','a')
    fh3=open('guests.txt','a')
    lin=fh1.readlines()
    for i in name:
        lin[5]='Dear '+i+',\n'
        lin[16]=n
        fh2.writelines(lin)
        fh3.write(i+'\n')
    fh2.close()
    fh1.close()

x=input('enter names of guests as a list ').split(',')
n=input('enter your name ')
invite(x)
