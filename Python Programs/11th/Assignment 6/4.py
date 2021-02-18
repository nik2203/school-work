s1=input('Enter a string ')
s2=input('Enter another string ')
if s1 in s2:
    print('String 2 without string 1 is '+s2.replace(s1,''))
else:
    print('String 1 is not present in string 2')
