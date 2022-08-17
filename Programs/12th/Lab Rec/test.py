cap='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
vow='aeiou'
spec='!"\'#~-+=_$%&*()@?/][}{;:.,><'

x=input('Do you want to begin (y/n)\n')
while x=='y' or x=='Y':
    ins=input('Enter a string \n')
    capc=0
    vowc=0
    specc=0
    numc=0
    for i in ins:
        if i in cap:
            capc+=1
            if i.lower() in vow:
                vowc+=1
        elif i in vow:
            vowc+=1
        elif i in spec:
            specc+=1
        elif i.isnumeric():
            numc+=1
    print('There are\n',
        capc,'Capital letters\n',
        vowc,'Vowels\n',
        specc,'Special Characters\n',
        numc,'Numbers\n In the string '+ins)
    x=input('Do you want to continue (y/n)\n')