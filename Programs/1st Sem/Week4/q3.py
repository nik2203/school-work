a=int(input('Enter a number\n'))
b=int(input('Enter a number\n'))
c=int(input('Enter a number\n'))
if ((a**2)+(b**2)==(c**2)) or ((a**2)+(c**2)==(b**2)) or ((b**2)+(c**2)==(a**2)):
    print('The numbers are pythagorean triplets')
else:
    print('The numbers are not pythagorean triplets')
