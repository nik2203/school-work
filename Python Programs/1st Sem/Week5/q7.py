ut=[]
rep=[]
tup=eval(input('Enter a tuple of items\n'))
for i in tup:
    if i not in ut:
        ut.append(i)
    elif i in ut and i not in rep:
        rep.append(i)
print('The repeated items are',rep)
