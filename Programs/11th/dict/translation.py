english={'red':'red','pink':'pink','orange':'orange',\
              'yellow':'yellow','green':'green','blue':'blue','purple':'purple'}
french={'red':'rouge','pink':'rose','orange':'orange','yellow':'jaune',\
             'green':'vert','blue':'bleu','purple':'violet'}
spanish={'red':'rosso','pink':'rosa','orange':'arancione','yellow':'giallo'\
              ,'green':'verde','blue':'azzurro','purple':'viola'}
italian={'red':'rojo','pink':'rosa','orange':'naranja','yellow':'amarillo'\
              ,'green':'verde','blue':'azul','purple':'violeta'}
t1=input('enter language you are translating from ')
t2=input('enter language you are translating to ')
col=input('enter color you are translating ')
if col in t1.values():
    
