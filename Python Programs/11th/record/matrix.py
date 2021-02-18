a=[]
b=[]
x=int(input('Enter no. of rows of matrixes '))
y=int(input('Enter no. of columns of matrixes '))
res=[]
for i in range(x):
    a.append([])
    b.append([])
    res.append([])
    for j in range(y):
        res[i].append(0)
for i in range(0,x):
    for j in range(0,y):
        inp=int(input('Enter elements of matrix 1 '))
        a[i].append(inp)
for i in range(0,x):
    for j in range(0,y):
        inp=int(input('Enter elements of matrix 2 '))
        b[i].append(inp)
ctr=int(input('Do you want to:\n1.Add\n2.Subtract\n3.Multiply '))
if ctr>3:
    print('Invalid input')
if ctr==1:
    for i in range(x):
        for j in range(y):
            res[i]=(a[i][j]+b[i][j])
    print(res)
if ctr==2:
    for i in range(x):
        for j in range(y):
            res[i]=(a[i][j]-b[i][j])
    print(res)
if ctr==3:
    for i in range(x):
        for j in range(y):
            for k in range(x):
                res[i][j]+=a[i][k]*b[k][i]
    print(res)
