#Discount
a=float(input('Enter price of product 1 '))
b=float(input('Enter price of product 2 '))
c=float(input('Enter price of product 3 '))
x=int(input('Enter quantity of product 1 '))
y=int(input('Enter quantity of product 2 '))
z=int(input('Enter quantity of product 3 '))
total=a*x+b*y+c*z
if total>3000:
    print('The discount available is 10%, or rupees '+str(total*0.1) \
          +'\nThe net price after discount is '+str(total-(total*0.1)))
elif total>1500 and total<=3000 :
    print('The discount available is 5%, or rupees '+str(total*0.05) \
          +'\nThe et price after discount is '+str(total-(total*0.05)))
elif total<1500:
    print('No discount is avaialable')
