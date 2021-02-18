n=int(input('Enter monthly income '))
AI=n*12
if AI>=600000:
    print('The tax rate is 8% and tax paid is, ',AI*0.08)
elif 600000>AI>=300000:
    print('The tax rate is 6% and tax paid is, ',AI*0.06)
elif 300000>AI>=150000:
    print('The tax rate is 2% and tax paid is ',AI*0.02)
else:
    print('No tax is to be paid')
