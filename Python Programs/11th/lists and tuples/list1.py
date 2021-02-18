import random
a=['black widow','iron man','odinson','mighty thor','namor','captain america',
   'hope van dyne','scott lang','hank pym','janet van dyne','kate bishop',
   'black panther','storm','beast','venom','agent venom','quake','clint barton',
   'mockingbird','spider man','spider woman','captain marvel','miss marvel',
   'amadeus cho','red hulk','hulk','she hulk','daredevil','jessica jones',
   'luke cage','iron fist','doctor strange','quicksilve','scarlett witch',
   'miles morales','iron heart','vision','hercules','sentry','ares','athena',
   'zeus','mantis','star lord','gamora','groot','rocket racoon','nebula',
   'hellcat','wonder man','falcon','tigra','spectrum','war machine','the thing',
   'mr. fantastic','human torch','moon night','invisible woman','quasar','sersi',
   'sandman','crystal','dark hawk','firestar','wolverine','echo','cassie lang',
   'nova','sharon carter','valkyrie','goliath','giant man','noh varr',
   'captain britain','shang chi','captain universe','hyperion','doctor octopus',
   'black bolt','america chavez','gwenpool','white tiger','wiccan','hulkling',
   'squirrel girl','songbird','blue marvel','star brand','sabretooth','cable',
   'singularity','medusa','sister grimm','robbie reyes','fuse','kid omega','alloy',
   'elektra','punisher','yellowjacket','swordsman','yondu','speed','x-23','hazmat',
   'black ant','deadpool','dazzler','victor mancha','doombot','rogue']
r=[]
for i in range(0,len(a)//2):
    x=random.randint(0,len(a)-1)
    r.append(a[x])
print(r)
    
