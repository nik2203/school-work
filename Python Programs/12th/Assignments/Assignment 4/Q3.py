with open('hex.txt','r+') as hexd:
    read=hexd.read()
    pos1=read.find('2A')+1
    pos2=read.find('2E')+1
    strw=read[read.find('3A')+1:]+'3F Question Mark\n'
    hexd.seek(pos1)
    hexd.write('2A ASTERIKS')
    hexd.seek(pos2)
    hexd.seek(read.find('3A'))
    hexd.write(strw)
    
    
    
    
