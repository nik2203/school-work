import math, random, string

def genotp():
    digits='0123456789'
    otp='' 
    for i in range(4) : 
        otp+=digits[math.floor(random.random() * 10)] 
    return otp

def gencap():
    size=int(input('enter size of captcha '))
    generate_cap=''.join([random.choice( string.ascii_uppercase+
                                           string.ascii_lowercase +
                                           string.digits+
                                           string.punctuation)  
                                            for n in range(size)])  
                             
    return generate_cap  

def valemail():
    x=input('enter an email ')
    try:
        l=x.split('@')
        if l[1] in ['gmail.com','googlemail.com','yahoomail.com','rediffmail.com']:
            ctr='True'
        else:
            ctr='False'
    except:
        print('This is not a valid email')
    else:
        if ctr=='True':
            print('This is a valid email')
        elif ctr=='False':
            print('This is an invalid email')
