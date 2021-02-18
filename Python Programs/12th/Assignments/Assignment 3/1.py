import validate

n=input('would you like to:\n'
        '1. Generate an OTP\n'
        '2. Generate a CAPTCHA\n'
        '3. Check the validity of an email\n')
if n=='1':
    ot=validate.genotp()
    print('Your OTP is:',ot)
if n=='2':
    ca=validate.gencap()
    print('Your CAPTCHA:',ca)
if n=='3':
    validate.valemail()
