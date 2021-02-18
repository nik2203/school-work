def showmodels():
    print('Available models:\n'
          'SUVs:\n'
          'Q2, Q3, Q4, Q5, Q6, Q7, Q8\n'
          'Hatchbacks:\n'
          'A1, A3, A4\n'
          'Sedans:\n'
          'A5, A6, A7, A8\n'
          'Coupes:\n'
          'TT, TTS Roadster\n'
          'Sports:\n'
          'RS Series, R8')

if __name__=='__main__':
    x=input('Would you like to see our models ')
    if x in ['Yes','yes','y']:
        showmodels()
    else:
        print('Thank you')
              
