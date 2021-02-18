def transp(ar,res):
    for i in range(len(ar)):
        for j in range(len(ar[0])):
            res[j][i]=ar[i][j]
    return res
def ma_ma(r,c):
    res=[]
    for i in range(r):
        res.append(['0']*c)
    return res
    
ar=eval(input('enter a matrix '))
r=int(input('enter number of rows '))
c=int(input('enter number of columns'))

print(transp(ar,ma_ma(r,c)))
