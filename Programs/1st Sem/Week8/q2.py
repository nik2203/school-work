def rev(st):#defining function
    if len(st)==0:#if coditon to check the length of the string 
        return st
    else:
        return rev(st[1:])+st[0]#reverses the string 

st=input('Enter a string to reverse \n')
print(rev(st))#calling function 