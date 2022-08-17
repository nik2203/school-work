G = 6.673*(10**(-11))

m1=int(input('Enter mass of body 1\n'))
m2=int(input('Enter mass of body 2\n'))
r=int(input('Enter distance between centres of two bodies\n'))

f=(G*m1*m2)/(r**2)
print(round(f,2))
