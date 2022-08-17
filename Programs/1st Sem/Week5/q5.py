mat=eval(input('Enter a 2D list, i.e, of the form [[],[],[]]\n'))
s=0
for i in range(len(mat)):
    s+=mat[i][i]
print('The sum of the diagonal elements of the matrix is,',s)