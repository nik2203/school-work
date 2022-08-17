s=input('Enter a string (no symbols) ')
cons=0
vowels=0
digits=0
for i in range(0,len(s)):
    if ord(s[i])>47 and ord(s[i])<58 :
        digits+=1
    elif s[i]=='a' or s[i]=='e' or\
         s[i]=='i' or s[i]=='o' or\
         s[i]=='u' or s[i]=='A' or\
         s[i]=='E' or s[i]=='I' or\
         s[i]=='O' or s[i]=='U':
        vowels+=1
    else:
        cons+=1
print('There are',cons,'consonants,',vowels,'vowels'\
      ' and',digits,'digits')
