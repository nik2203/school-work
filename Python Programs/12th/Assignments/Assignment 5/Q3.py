import pickle
import os

col1={'WHITE':'#FFFFFFF','SILVER':'#C0C0C0','GRAY':'#808000',}
col2={'BLACK':'#000000','RED':'#FF0000','MAROON':'#800000'}
col3={'YELLOW':'#FFFF00','OLIVE':'#808000','LIME':'#00FF00'}
l=[col1,col2,col3]


fh=open('colours.bin','wb')
for i in l:
    pickle.dump(i,fh)
fh.close()

#b
fh=open('colours.bin','ab+')
pickle.dump({'GREEN':'#008000'},fh)
fh.seek(0)
fh.close()

#c
fh1=open('colours.bin','rb')
fh2=open('temp.bin','wb')
while True:
    try:
        a=pickle.load(fh1)
        if 'GRAY' in a.keys():
            a['GRAY']='#808080'
            pickle.dump(a,fh2)
        else:
            pickle.dump(a,fh2)
    except EOFError:
        break
fh1.close()
fh2.close()
os.remove('colours.bin')
os.rename('temp.bin','colours.bin')
