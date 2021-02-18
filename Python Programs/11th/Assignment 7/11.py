s=input('Enter a string ')
a=0
b=''
for i in range(0,len(s)):
    for j in range(i,len(s)):
        if s[j] in b:
            continue
        elif s[j]==s[i]:
            a+=1
    b+=s[i]
    if a!=0:
        print(b[i],a,sep=' ',end='\n')
        a=0
