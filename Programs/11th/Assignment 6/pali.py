n=int(input('Enter a number (below 6 digits)'))
ctr=0
while ctr<7:
    for i in range(2,7):
        if n%10==n**(i-1):
            print('It is a palindrome')
            break
        else:
            ctr+=1
else:
    print('It is not a palindrome')

