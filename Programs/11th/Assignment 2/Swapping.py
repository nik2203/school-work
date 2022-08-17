#Swapping two numbers

#Using temporary variables
a=input('Enter a number ')
b=input('Enter a number ')
t=a
a=b
b=t
print(a)
print(b)

#Without using temporary variables

#Assignment Swap
a=input('Enter a number ')
b=input('Enter a number ')
a,b=b,a
print(a)
print(b)

#Using Arithmetic Operators
a=int(input('Enter a number '))
b=int(input('Enter a number '))
a=a+b
b=a-b
a=a-b
print(a)
print(b)

#Using XOR
a=int(input('Enter a number '))
b=int(input('Enter a number '))
a=a^b
b=a^b
a=a^b
print(a)
print(b)
