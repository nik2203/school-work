s=input('Enter a string ')
n=int(input('Enter shift '))%26
for i in range(len(s)):
    if (ord(s[i])+n>64 and ord(s[i])+n<91)or\
       (ord(s[i])+n>96 and ord(s[i])+n<123):
        print(chr(ord(s[i])+n),end='')
    elif ord(s[i])==32:
        print(s[i],end='')
    else:
        print(chr(ord(s[i])+n-26),end='')
