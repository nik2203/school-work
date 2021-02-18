s=input('Enter a string ')
s1=s.find('not')
s2=s.find('poor')
if s1>s2:
    print(s)
elif s2>s1:
    s3=s.find('bad')
    if s3>s2:
        print(s.replace(s[s1:s3+3],'good'))
        
