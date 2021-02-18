def merge(ar1,ar2):
    ar3=[]
    for i in ar1:
        if i%2!=0:
            ar3.append(i)
    for i in ar2:
        if i%2!=0:
            ar3.append(i)
    for i in ar1[::-1]:
        if i%2==0:
            ar3.append(i)
    for i in ar2[::-1]:
        if i%2==0:
            ar3.append(i)
    return ar3

ar1=eval(input('enter an array '))
ar2=eval(input('enter an array '))
print(merge(ar1,ar2))
