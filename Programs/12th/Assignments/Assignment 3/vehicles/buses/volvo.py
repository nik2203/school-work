def showmodels():
    print('Available models:\n'
          '9400 B8R, 9400 B11R Multi Axle, 8400 City Bus, 9400, Hybrid City Bus')

if __name__=='__main__':
    x=input('Would you like to see our models ')
    if x in ['Yes','yes','y']:
        showmodels()
    else:
        print('Thank you')
              
