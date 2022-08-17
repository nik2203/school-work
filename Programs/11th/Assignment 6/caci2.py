s=input('Enter a string (lower case) ')
n=int(input('Enter shift '))
di=input('Enter the direction of shift (l/r)')
l=list(s)
for i in range(0,len(l)):
    a=ord(l[i])
    if di=='l' and(a-97)>n \
       and(a>=97 and a<=122):
        l[i]=chr(a-n)
    elif di=='l' and(a-97)<n and(a>=97 and a<=122):
        l[i]=chr(a+25-n+1)
    if (a<97 or a>122)\
       and(a<65 or a>90):
        pass
    elif di=='r' and(122-a)>n and(a>=97 and a<=122):
         l[i]=chr(a+n)
    elif di=='r' and (122-a)<n\
          and(a>=97 and a<=122):
        l[i]=chr(a-25+n-1)
for i in range(0,len(l)):
    print(l[i],end='')
