def url_chan(ar):
    res=[]
    for i in ar:
        if i[0:7]!='http://':
            res.append('http://'+i)
        else:
            res.append(i)
    return res

ar=eval(input('enter list of urls '))
print(url_chan(ar))
