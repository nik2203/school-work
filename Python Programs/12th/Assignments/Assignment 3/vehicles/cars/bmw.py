def showmodels():
    print('Available models:\n'
          'SUVs:\n'
          'X1, X2, X3, X4, X5, X6, X7\n'
          'Sedans:\n'
          '3 Series, 5 Series, 7 Series, 3 Series GT, 6 Series GT\n'
          'Coupes:\n'
          '8 Series\n'
          'Sports:\n'
          'M2, M5, M760Li, Z4 M40i')

if __name__=='__main__':
    x=input('Would you like to see our models ')
    if x in ['Yes','yes','y']:
        showmodels()
    else:
        print('Thank you')
              
