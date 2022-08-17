def check_pal(x,i,l) :
    if len(x)==0:
        return True
    if (i==l): 
        return True
    if (x[i]!=x[l]) : 
        return False
    if (i<l+1) : 
        return check_pal(x,i+1,l-1)
    return True

y=input('enter a string to check palindrome for ')
if(check_pal(y,0,len(y)-1)):
    print('it is a palindrome')
else:
    print('it is not a palindrome')
