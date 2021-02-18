s=input('Enter a string ')
l=list(s)
a=0
while a<len(s) :
    l[a]=chr(ord(l[a])-32)
    a=s.find(' ',a,len(s))
    l[a]=chr(ord(1[a])-32)
x=s[0]
for i in range(0,len(l)):
    x+=str(l[i])
print(x)
