s=input('Enter a URL ')
x=s.find(':')
pro=s[:x:]
dom=s[x+3:s.find('/',x+3):]
fold=s[s.find('/',x+3,len(s)-1)+1::]
print('The protocol is '+pro+', the domain'\
      ' is '+dom+' and the folder name is '+fold)
