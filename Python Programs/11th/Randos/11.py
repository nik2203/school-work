#bubble sort
l=[12,313,6,10,48,33,5,19,2]
for i in range(len(l)-1):
    for j in range(i+1):
        for k in range(len(l)-1):
            if l[k]>l[k+1]:
                l[k],l[k+1]=l[k+1],l[k]
print(l)

#insertion sort
l=[12,313,6,10,48,33,5,19,2]
x=l.sort
for i in range(1,len(l)):
    key=l[i]
    j=i-1
    while j >=0 and key<l[j]:
        l[j+1]=l[j]
        j-=1
    l[j+1]=key
print(l)

#selection
l=[('math',70),('eng',78),('phys',69),('chem',72),('comp',75)]
for i in range(len(l)):
    min_id=i
    for j in range(i+1,len(l)):
        if l[min_id][1]>l[j][1]:
            min_id=j
    l[i],l[min_id]=l[min_id],l[i]
print(l)


