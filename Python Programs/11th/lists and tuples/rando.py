x=eval(input('enter list '))
y=eval(input('enter list '))
result=[[x[i][j]+y[i][j]
         for j in range(len(x[0]))] for i in range (len(x))]
for r in result:
    print(r)
