x=eval(input('Enter a tuple of numbers '))
y=eval(input('Enter a tuple of numbers '))
z=[]
for i in range(len(x)):
    if (x[i]%2==0):
        z.append(x[i])
for i in range(len(y)):
    if (y[i]%2==0) and y[i] not in z:
        z.append(y[i])
print(tuple(z))
