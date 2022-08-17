s=input('Enter a string ')
n=int(input('Enter shift '))
di=input('Enter the direction of shift (l/r)')
l=list(s)
for i in range(0,len(l)):
    a=ord(l[i]
    if di=='l' and a>n and((a>=97\
       and a<=122) or (a>=65 and a<=90))
          [i]==chr(a-n)
        if (a<97 or a>122)\
           and(a<65 or a>90):
            pass
    elif di=='r':
        print('home')
for i in range(0,len(l)):
    print(l[i],end='')
