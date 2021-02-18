def sq_sum(x):
    t=0
    while x>0:
        t+=(x%10)**2
        x//=10
    return t

def is_hap(x):
    seen=[]
    while x>1 and x not in seen:
        seen.append(x)
        x=sq_sum(x)
    if x==1:
        return True
    elif x in seen:
        return False

n=int(input('enter a number '))
if is_hap(n):
    print(n,'is a happy number')
else:
    print(n,'is not a happy number')
