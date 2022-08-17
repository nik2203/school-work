s=input('Enter a string with no symbols ')
vow=0
con=0
dig=0
for i in range(len(s)):
    if ord(s[i])<58 and ord(s[i])>47:
        dig+=1
    elif s[i] in 'qwrtypsdfghjklzxcvbnm':
        con+=1
    elif s[i] in 'aeiou':
        vow+=1
print('There are',vow,'vowels,',dig,'digits and',con,'consonants')
    
