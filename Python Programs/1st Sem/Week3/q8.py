import random
#a
s=input('Enter a random string\n')
ra=random.choice(s)
print(ra)

#b
#i
clas=[1,2,3,5,6,7,8,9,10]
print(clas)
random.shuffle(clas)
print('After shuffling',clas)

#ii
rep=random.choice(clas)
print('The clas representative would be',rep)

#iii
x=random.sample(clas,2)
print('The event co-ordinators will be',x)

#c
a=float(input('Enter a float number\n'))
b=float(input('Enter a float number\n'))
res=a*b
print('The product of',a,'and',b,'is',res)