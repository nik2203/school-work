def showmodels():
    print('Available models:\n'
          'LPO 1623, LP 410, LP 712, LP 912, LPO 1624')

if __name__=='__main__':
    x=input('Would you like to see our models ')
    if x in ['Yes','yes','y']:
        showmodels()
    else:
        print('Thank you')
              
