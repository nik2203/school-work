#roots of a quadratic equation
a=float(input('Enter x^2 coefficient '))
b=float(input('Enter x coefficient '))
c=float(input('Enter constant '))
d=(b**2)-4*a*c
if a==0:
    print('Invalid input')
elif d<0 :
    print('The roots are imaginary \n'+str((-b+d**0.5)/2*a)\
          +' and '+str((-b-d**0.5)/2*a))
elif d==0 :
    print('The roots are real and equal \n'+str((-b+d**0.5)/2*a)\
          +' and '+str((-b-d**0.5)/2*a))
else :
    print('The roots are real and distinct \n'+str((-b+d**0.5)/2*a)\
          +' and '+str((-b-d**0.5)/2*a))
