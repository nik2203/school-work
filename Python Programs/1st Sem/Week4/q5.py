import math

a=int(input('Enter a number a\n'))
b=int(input('Enter a number b\n'))
c=int(input('Enter a number c\n'))
d=(b**2)-(4*a*c)
if d>0:
    r1=(-b+math.sqrt(d))/(2*a)
    r2=(-b-math.sqrt(d))/(2*a)
elif d==0:
    r1=r2=-b/(2*a)
else:
    r1=complex(-b/2*a,((-d)**0.5)/2*a)
    r2=complex(-b/2*a,-((-d)**0.5)/2*a)
if type(r1)==complex:
    print('The roots are',round(r1.real,2),'+',r1.imag,'and',round(r2.real,2),'-',r2.imag)
else:
    print('The roots are',round(r1,2),'and',round(r2,2))
