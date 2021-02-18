x=int(input('Enter length of tuple '))
l=[]
for i in range(x):
    s=str(input('Enter a string '))
    l.append(s)
print(tuple(l[::-1]))
