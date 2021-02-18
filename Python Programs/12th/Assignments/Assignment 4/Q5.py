with open('user.txt','r+') as user_base:
    l=user_base.read().split(',')
    user_base.seek(0)
    read=user_base.read()
    u=input('enter username ')
    for i in range(0,len(l)+1,2):
        if l[i]==u:
            passw=l[i+1]
            p=input('enter password ')
            if p == passw:
                print('You have entered the right username and password')
            else:
                print('The password does not match the username')
            break
        else:
            user_base.seek(len(read)+7)
            p=input('enter your password ')
            user_base.write('\n'+u+','+p)
            print('you are now a valid user')
            break
