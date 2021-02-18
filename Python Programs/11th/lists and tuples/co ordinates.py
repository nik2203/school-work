x=int(input('Enter no. of points to check '))
l=[]
for i in range(x):
    l.append([])
for i in range(x):
    for j in range(1):
        y=int(input('enter x cordinate '))
        ordi=int(input('enter y coorindate '))
        l[i].append(y)
        l[i].append(ordi)
print(tuple(l))
for i in range(x):
    initial=l[i]
    for j in range(i+1,len(l)+1):
        
        
