import urllib.request

x=input('Enter the URL of the website ')
sourcod=urllib.request.urlopen(x)
html=sourcod.read()
index=0
l=[]
while index<=0:
    inst=html.find('href')
    l=html[inst]
    index=-1
for i in l:
    print(i)
''' I didn't get the proper code for this '''
