def rev(st):
    if len(st)==0:
        return st
    else:
        return rev(st[1:])+st[0]

st=input('Enter a string to reverse \n')
print(rev(st))