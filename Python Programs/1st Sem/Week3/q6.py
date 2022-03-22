sh=6
sm=52
st=(sh*3600)+(sm*60)
pace1=(8*60)+15
pace2=(7*60)+12
tt=(pace1*2)+(pace2*3)
tth=tt//3600
ttm=tt//60
etm=(sm+ttm)%60
eth=(sm+ttm)//60
eh=sh+tth+eth
print('The person returns home for breakfast at',str(eh)+':'+str(etm))