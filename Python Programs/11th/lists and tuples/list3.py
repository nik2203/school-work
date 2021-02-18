encoded=eval(input('Enter list of encoded messages '))
deco=[]
for i in encoded:
    if len(i)>5:
        continue
    else:
        if (i[0]=='a'or'A')and(i[4]=='z'or'Z'):
            deco.append(i[1:4])
print(deco)
